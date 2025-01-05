from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Task
from django.db import connection, DatabaseError
from django.contrib import messages
from .forms import TaskForm
from django.contrib.auth import login


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = request.POST['first_name']
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def task_list(request):
    completed = request.GET.get('completed', None)
    if completed is not None:
        tasks = Task.objects.filter(user=request.user, completed=bool(int(completed)))
    else:
        tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

def insert_task(user_id, title, description):
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO todo_app_task (user_id, title, description, created_at, completed)
            VALUES (%s, %s, %s, DATETIME('now'), %s)
            """,
            [user_id, title, description, False]
        )

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        insert_task(request.user.id, title, description)
        return redirect('task_list')
    return render(request, 'add_task.html')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')

@login_required
def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def fetch_all_tasks(user_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM todo_app_task WHERE user_id = %s", [user_id])
            rows = cursor.fetchall()
        return rows
    except DatabaseError as e:
        print(f"Database error: {e}")
        return []

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'edit_task.html', {'form': form, 'task': task})