from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProjectForm, MessageForm
from .models import Project, Skill, Message


# Create your views here.

def home(request):
    projects = Project.objects.all()
    detailedskills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')

    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment was successfully added!')

    context = {'projects': projects, 'skills': skills, 'detailedSkills': detailedskills, 'form': form}

    return render(request, 'base/home.html', context)


def projectPage(request, pk):
    projectObj = Project.objects.get(id=pk)

    return render(request, 'base/project.html', {'project': projectObj})


def addProject(request):
    forms = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': forms}
    return render(request, 'base/project_form.html', context)


def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)


def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')

    UnreadCount = Message.objects.filter(is_read=False).count()
    context = {'inbox': inbox, 'unreadCount': UnreadCount}
    return render(request, 'base/inbox.html', context)


def MessagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message': message}
    return render(request, 'base/message.html', context)
