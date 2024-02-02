from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from .models import Task
from .forms import TaskForm, LoginForm
from .forms import RegistrationForm
from django.urls import reverse_lazy



@login_required
def user_dashboard(request):
    # Retrieve tasks assigned to the logged-in user
    user_tasks = Task.objects.filter(assigned_to=request.user)
    # all_tasks = Task.objects.all()
    user_name = request.user.username

    tasks_todo = Task.objects.filter(status='ToDo', assigned_to=request.user)
    tasks_in_progress = Task.objects.filter(status='InProgress', assigned_to=request.user)
    tasks_in_review = Task.objects.filter(status='InReview', assigned_to=request.user)
    tasks_completed = Task.objects.filter(status='Completed', assigned_to=request.user)



    context = {
        'user_tasks': user_tasks,
        # 'all_tasks': all_tasks,
        'user_name': user_name,
        'tasks_todo': tasks_todo,
        'tasks_in_progress': tasks_in_progress,
        'tasks_in_review': tasks_in_review,
        'tasks_completed': tasks_completed,

    }
    return render(request, 'board/user_dashboard.html', context)


@login_required
def assign_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_to = request.user
            task.save()
            return redirect('user_dashboard')
    else:
        form = TaskForm()

    return render(request, 'board/assign_task.html', {'form': form})


def all_users_tasks(request):
    # Retrieve all tasks assigned to all users
    all_tasks = Task.objects.all()
    tasks_todo = Task.objects.filter(status='ToDo')
    tasks_in_progress = Task.objects.filter(status='InProgress',)
    tasks_in_review = Task.objects.filter(status='InReview', )
    tasks_completed = Task.objects.filter(status='Completed',)
    assigned_user = Task.objects.filter(assigned_to=request.user)


    context = {
        'tasks_todo': tasks_todo,
        'tasks_in_progress': tasks_in_progress,
        'tasks_in_review': tasks_in_review,
        'tasks_completed': tasks_completed,
        'assigned_user' : assigned_user,
        'all_tasks': all_tasks
    }

    

    return render(request, 'board/all_users_task.html', context)



class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'board/login.html'



class CustomLogoutView(LogoutView):
    # You can customize the logout view here if needed
    next_page = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        print("CustomLogoutView get method")
        return super().get(request, *args, **kwargs)



def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')
    else:
        form = RegistrationForm()

    return render(request, 'board/register_user.html', {'form': form})


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Use the existing TaskForm
        if form.is_valid():
            form.save()
            return redirect('user_dashboard')
    else:
        form = TaskForm(instance=task)  # Use the existing TaskForm

    return render(request, 'board/assign_task.html', {'form': form, 'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('user_dashboard')

    return render(request, 'board/delete_task.html', {'task': task})

def transition_task(request, task_id, target_status):
    task = get_object_or_404(Task, id=task_id)

    # Update the task's status
    task.status = target_status
    task.save()

    return redirect('user_dashboard')


# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             user = User.objects.get(username = username)
#         except:
#             messages.error(request, 'User does not exist')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('user_dashboard')
#         else:
#             messages.error(request, 'Username or Password does not exist')
        

#     context = {}
#     return render(request, 'board/login.html', context)