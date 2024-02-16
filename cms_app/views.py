from rest_framework import viewsets
from django.shortcuts import render, redirect
from .models import Admin, Author
from .serializers import AdminSerializer, AuthorSerializer
from django.http import HttpResponse
from .forms import AdminForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login,logout
from .forms import AdminForm, LoginForm
from django.db import models
from django.contrib.auth import get_user_model






class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

def home(request):
    content_items = Author.objects.all()
    return render(request, 'home.html', {'content_items': content_items})


def search(request):
    query = request.GET.get('q', '')
    print(f"Search query: {query}")

    results = Author.objects.filter(author__username__icontains=query) | \
              Author.objects.filter(author__email__icontains=query) | \
              Author.objects.filter(author__first_name__icontains=query) | \
              Author.objects.filter(author__last_name__icontains=query)
    print(f"Results: {results}")

    return render(request, 'search.html', {'results': results, 'query': query})




def success_page(request):
    return render(request, 'registration/success_page.html')

def register_user(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            authenticated_user = authenticate(request, username=user.username, password=form.cleaned_data['password'])

            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('success_page')  # Redirect to the success page
            else:
                # Handle authentication failure (e.g., display an error message)
                return render(request, 'registration/register_user.html', {'form': form, 'error_message': 'Authentication failed'})

    else:
        form = AdminForm()

    return render(request, 'registration/register_user.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with the desired URL after login
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')  