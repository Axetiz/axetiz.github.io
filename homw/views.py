from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

# Define a view function for the home page


def logout_view(request):
    logout(request)
    return redirect('index')

def home(request):
    return render(request, 'index.html')

def ui(request):
    return render(request, 'ui.html')

def game(request):
    return render(request, 'startplaying.html')
def opponent(request):
    return render(request, 'opponent.html')
def gamemenu0(request):
    return render(request, 'gamemenu0.html')
def gamemenu1(request):
    return render(request, 'gamemenu1.html')

def gamecomp_algebra(request):
    return render(request, 'gamecomp_algebra.html')
def gamecomp_calculus(request):
    return render(request, 'gamecomp_calculus.html')
def gamecomp_combinatorics(request):
    return render(request, 'gamecomp_combinatorics.html')
def gamecomp_discrete_mathematics(request):
    return render(request, 'gamecomp_discrete_mathematics.html')
def gamecomp_geometry(request):
    return render(request, 'gamecomp_geometry.html')

def gamechell_algebra(request):
    return render(request, 'gamechell_algebra.html')
def gamechell_calculus(request):
    return render(request, 'gamechell_calculus.html')
def gamechell_combinatorics(request):
    return render(request, 'gamechell_combinatorics.html')
def gamechell_discrete_mathematics(request):
    return render(request, 'gamechell_discrete_mathematics.html')
def gamechell_geometry(request):
    return render(request, 'gamechell_geometry.html')


@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
def profile_edit(request):
    # Placeholder for profile editing logic
    return render(request, 'editprofile.html')
# Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/home/')

    # Render the login page template (GET request)
    return render(request, 'login.html')

# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)

        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')

        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        # Set the user's password and save the user object
        user.set_password(password)
        user.save()

        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')

    # Render the registration page template (GET request)
    return render(request, 'register.html')
