from django.shortcuts import render

# Create your views here.
def about_me_view(request):
    return render(request, 'portfolio/about.html')

def projects_view(request):
    return render(request, 'portfolio/projects.html')

def experience_view(request):
    return render(request, 'portfolio/experience.html')

def contact_view(request):
    return render(request, 'portfolio/contact.html')