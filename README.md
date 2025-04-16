# **Django To-Do Application**

A simple and user-friendly To-Do app built using the Django framework. This application allows users to register, log in, and manage their tasks effectively, including adding, editing, marking as complete, and deleting tasks. It also features user authentication and a responsive interface powered by Bootstrap.

---

## **Features**
- **User Authentication**: Secure registration and login/logout functionality.
- **Task Management**: Create, edit, mark as complete/incomplete, and delete tasks.
- **Responsive Design**: Bootstrap-powered interface for mobile, tablet, and desktop views.
- **User-Specific Tasks**: Each user can only view and manage their own tasks.

---

## **Technologies Used**
- **Backend**: Django 5.1.4
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite3
- **Other Dependencies**: Python, Django forms

---

# 🛠️ How to Run the Django Todo Project

This guide will help you set up and run the Django-based Todo project on your local machine.

---

## ✅ Prerequisites

Make sure you have the following installed:

- Python (3.x)
- pip
- Virtualenv (recommended)

---

## 📦 Project Setup Steps

### 1. Clone or Download the Project

```bash
git clone (https://github.com/SamarthMule/todo_project.git)
cd todo_project

python -m venv venv
# Activate the virtual environment:
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate         # For Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser # Optional

python manage.py runserver
```
##Project Structure 
todo_project/
│

├── todo_app/                  # Main application folder

├── todo_project/              # Django project settings folder

├── manage.py                  # Django management script

├── requirements.txt           # Project dependencies

├── README.md                  # Project documentation

└── .gitignore                 # Files/folders to be ignored by Git

