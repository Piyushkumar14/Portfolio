from django.shortcuts import render
from .models import Project, Skill


# Create your views here.

def home(request):
    projects = Project.objects.all()
    detailedskills = Skill.objects.exclude(body = '')
    skills = Skill.objects.filter(body = '')


    context = {'projects': projects, 'skills': skills, 'detailedSkills': detailedskills}

    return render(request, 'base/home.html', context)

def projectPage(request, pk):
    projectObj = Project.objects.get(id=pk)

    return render(request, 'base/project.html', {'project': projectObj})

def addProject(request):
    context = {}
    return render(request, 'base/project_form.html', context)