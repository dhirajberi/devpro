from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)

def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    context = {'project': project, 'tags': tags}
    return render(request, 'single-project.html', context)

def createProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    form = ProjectForm()
    context = {'form': form}
    return render(request, 'form-template.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    form = ProjectForm(instance = project)
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {}
    return render(request, 'projects/delete_obj.html', context)