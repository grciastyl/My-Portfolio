from django.shortcuts import render
from . import models

# Create your views here.

# Create your views here.
def projects_view(request):
    projects_list = models.Project.objects.all() #get all my projects from the database
    context={"projects": projects_list} # organize with a dictionary with key "project" and value projects_list
    return render(request, 'projects/projects.html', context) #pass the context to the template



