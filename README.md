
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

![image-20250415075431770](/home/omar/.config/Typora/typora-user-images/image-20250415075431770.png)

### Registration Page

![image-20250415075513794](/home/omar/.config/Typora/typora-user-images/image-20250415075513794.png)

### Login Page

![image-20250415075529270](/home/omar/.config/Typora/typora-user-images/image-20250415075529270.png)

### Todo Page

![image-20250415075552241](/home/omar/.config/Typora/typora-user-images/image-20250415075552241.png)

### Edit Task

![image-20250415075632446](/home/omar/.config/Typora/typora-user-images/image-20250415075632446.png)

License
-------

Taskmate is licensed under the MIT License.

Acknowledgments
---------------

Taskmate was built using Django, a high-level Python web framework. Thanks to the Django team for creating such a great framework!
