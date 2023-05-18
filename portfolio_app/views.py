from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm, ConnectionForm
from django.contrib.gis.geos import Point
from .models import CustomUser, Project, Connection,Experience, Skill
from django.contrib.gis.db.models import Extent
from django.template import Context
from django.core import serializers

# Create your views here.

def home(request):
    """
    Renders the home(portfolio) page of the website.

    Retrieves all projects, skills, experiences, and the user's profile from the database.
    Orders experiences by start date in descending order and limits to the five most recent.
    Renders the 'home.html' template with the retrieved data and a connection form.

    """
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')[:5]
    profile = CustomUser.objects.all().first()
    form = ConnectionForm()
    context = {'projects': projects, 'skills': skills, 'form': form,'experiences':experiences,'profile':profile}
    return render(request, 'home.html', context=context)

@login_required
def profile(request):
    """
    Renders the profile page for the currently authenticated user.

    Retrieves the current user from the request object and renders the 'profile.html' template
    with the user object.

    """
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required
def edit_profile(request):
    """
    Renders the edit profile page for the currently authenticated user.

    Retrieves the current user from the request object and displays a form for editing
    the user's profile details. If the request method is POST, updates the user's details
    with the submitted form data and redirects to the profile page. If the request method
    is GET, renders the 'edit_profile.html' template with the form object.

    """
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def map(request):
    """
    Renders a map of all users with location data, accessible only to superusers.

    Retrieves all users with location data from the database and serializes them as JSON.
    Renders the 'map.html' template with the serialized user data.

    """
    users = CustomUser.objects.exclude(location=None)
    users_json = serializers.serialize('json', users)
    return render(request, 'map.html', {'users': users_json})

def contact(request):
    """
    Renders the contact page and handles form submissions.

    If the request method is POST, validates the submitted form data and creates a new
    Connection object with the data before redirecting to the home page.

    """
    if request.method == 'POST':
        form = ConnectionForm(request.POST)
        if form.is_valid():
            conn = Connection()
            conn.your_name = form.cleaned_data['name']
            conn.email = form.cleaned_data['email']
            conn.subject = form.cleaned_data['subject']
            conn.message = form.cleaned_data['message']
            conn.save()
            context={}
            return redirect('home')

    else:
        form = ConnectionForm()

    return redirect('home')




