
Taskmate
================

Taskmate is a task management web application built using Django, a high-level Python web framework. It allows users to create, edit, and delete tasks, as well as mark them as completed.

Project Description
-------------------

Taskmate is designed to be a simple and intuitive task management tool. It allows users to create tasks with a title and mark them as completed when they are finished with the ability to edit the task. The application also includes a login and logout system, allowing users to access their own tasks and keep them private.

Installation
------------

To install Taskmate, follow these steps:

1. Clone the repository using Git:
```
git clone https://github.com/omar-elhorbity/taskmate.git
```
2. Navigate to the project directory:
```
cd taskmate
```
3. Install the required dependencies using pip:
```
pip install -r requirements.txt
```
4. Create a new database for the application:
```
python manage.py migrate
```
5. Create a superuser account:
```
python manage.py createsuperuser
```
6. Start the development server:
```
python manage.py runserver
```
7. Open a web browser and navigate to `http://localhost:8000` to access the application.

Features
--------

* Task creation, editing, and deletion
* Task completion tracking
* Login and logout system
* User authentication and authorization

## Screenshots

### Home Page

![Screenshot from 2025-04-15 07-54-03](https://github.com/user-attachments/assets/2c3ab70d-8107-407a-8e5a-bd7641704248)

### Registration Page

![Screenshot from 2025-04-15 07-54-57](https://github.com/user-attachments/assets/ea4622ee-dba5-4539-94a7-e5e03ecb0e65)

### Login Page

![Screenshot from 2025-04-15 07-55-21](https://github.com/user-attachments/assets/46ba00cc-d439-4e00-b3ef-21860615535f)

### Todo Page

![Screenshot from 2025-04-15 07-55-42](https://github.com/user-attachments/assets/886d17d6-8753-4b16-9611-5ecde9ef6c08)

### Edit Task

![Screenshot from 2025-04-15 07-56-24](https://github.com/user-attachments/assets/04b8e0e7-2247-471f-8ea8-9c4b2f0cd020)

License
-------

Taskmate is licensed under the MIT License.

Acknowledgments
---------------

Taskmate was built using Django, a high-level Python web framework. Thanks to the Django team for creating such a great framework!
