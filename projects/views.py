from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_list(request):
    return render(request, 'projects/index.html')

def all_projects(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, 'projects/all_projects.html', {'projects': projects})

def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/project_details.html', {'project': project})