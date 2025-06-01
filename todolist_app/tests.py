from django.test import TestCase, Client
from django.contrib.auth.models import User
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.urls import reverse
import datetime

# Model Tests
class TaskListModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_task_with_priority_due_date(self):
        task_data = {
            'manager': self.user,
            'task': 'Test task model',
            'priority': 'High',
            'due_date': datetime.date(2024, 12, 31)
        }
        task = TaskList.objects.create(**task_data)
        self.assertEqual(task.task, 'Test task model')
        self.assertEqual(task.priority, 'High')
        self.assertEqual(task.due_date, datetime.date(2024, 12, 31))
        self.assertEqual(task.manager, self.user)

    def test_task_default_priority(self):
        task_data = {
            'manager': self.user,
            'task': 'Test default priority',
            'due_date': datetime.date(2024, 10, 10)
        }
        # Priority not provided, should use default 'Medium'
        task = TaskList.objects.create(**task_data)
        self.assertEqual(task.priority, 'Medium')

# Form Tests
class TaskFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='formuser', password='testpassword')

    def test_valid_form_with_priority_due_date(self):
        form_data = {
            'task': 'Test valid form',
            'priority': 'Low',
            'due_date': datetime.date(2025, 1, 15),
            'done': False
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors.as_text())

    def test_form_saves_priority_due_date(self):
        form_data = {
            'task': 'Test form save',
            'priority': 'High',
            'due_date': datetime.date(2025, 3, 20),
            'done': False
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
        # To save a ModelForm, we usually need a manager instance if it's part of the model
        # but not directly in the form's fields that are user-editable without commit=False
        # In this case, TaskForm *does not* include 'manager' directly.
        # The view handles assigning the manager. For testing form save directly:
        task = form.save(commit=False)
        task.manager = self.user # Simulate view behavior
        task.save()

        saved_task = TaskList.objects.get(pk=task.pk)
        self.assertEqual(saved_task.task, 'Test form save')
        self.assertEqual(saved_task.priority, 'High')
        self.assertEqual(saved_task.due_date, datetime.date(2025, 3, 20))
        self.assertEqual(saved_task.manager, self.user)

    def test_invalid_priority_choice(self):
        form_data = {
            'task': 'Test invalid priority',
            'priority': 'Very High',  # Not a valid choice
            'due_date': datetime.date(2025, 1, 1)
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('priority', form.errors)

    def test_invalid_due_date_format(self):
        form_data = {
            'task': 'Test invalid due date',
            'priority': 'Medium',
            'due_date': 'not-a-date'
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('due_date', form.errors)

# View Tests
class TaskViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='viewuser', password='testpassword')
        self.client.login(username='viewuser', password='testpassword')

        self.todolist_url = reverse('todolist')
        self.task_data_valid = {
            'task': 'View test task creation',
            'priority': 'High',
            'due_date': '2024-07-20' # Use YYYY-MM-DD string format for POST data
        }

    def test_todolist_view_post_create_task(self):
        response = self.client.post(self.todolist_url, self.task_data_valid)
        self.assertEqual(response.status_code, 302) # Redirect after successful creation
        self.assertTrue(TaskList.objects.filter(task='View test task creation').exists())
        created_task = TaskList.objects.get(task='View test task creation')
        self.assertEqual(created_task.priority, 'High')
        self.assertEqual(created_task.due_date, datetime.date(2024, 7, 20))
        self.assertEqual(created_task.manager, self.user)

    def test_edit_task_view_post_update_task(self):
        initial_task = TaskList.objects.create(
            manager=self.user,
            task='Initial task for edit',
            priority='Low',
            due_date=datetime.date(2024, 1, 1)
        )
        edit_url = reverse('edit_task', args=[initial_task.id])
        updated_data = {
            'task': 'Updated task name',
            'priority': 'Medium',
            'due_date': '2024-08-15',
            'done': True # Include 'done' as it's part of TaskForm's fields
        }
        response = self.client.post(edit_url, updated_data)
        self.assertEqual(response.status_code, 302) # Redirect after successful edit

        updated_task = TaskList.objects.get(pk=initial_task.pk)
        self.assertEqual(updated_task.task, 'Updated task name')
        self.assertEqual(updated_task.priority, 'Medium')
        self.assertEqual(updated_task.due_date, datetime.date(2024, 8, 15))
        self.assertTrue(updated_task.done)

    def test_todolist_view_get_form_in_context(self):
        response = self.client.get(self.todolist_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], TaskForm)

    def test_edit_task_view_get_form_populated(self):
        task_to_edit = TaskList.objects.create(
            manager=self.user,
            task='Task to populate edit form',
            priority='High',
            due_date=datetime.date(2024, 9, 10),
            done=False
        )
        edit_url = reverse('edit_task', args=[task_to_edit.id])
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], TaskForm)

        form_in_context = response.context['form']
        self.assertEqual(form_in_context.instance, task_to_edit)
        self.assertEqual(form_in_context.initial['priority'], 'High')
        self.assertEqual(form_in_context.initial['due_date'], datetime.date(2024, 9, 10))
        self.assertEqual(form_in_context.initial['task'], 'Task to populate edit form')
        self.assertEqual(form_in_context.initial['done'], False)
