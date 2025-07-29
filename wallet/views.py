from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import UploadedImage


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists.")
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('upload')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('upload')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'login.html')

@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        binary_data = image.read()
        Upload.objects.create(user=request.user, image_data=binary_data)
        return HttpResponse("Image uploaded successfully.")
    user_uploads = Upload.objects.filter(user=request.user)
    return render(request, 'upload.html', {'uploads': user_uploads})

def logout_view(request):
    logout(request)
    return redirect('home')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'admin123':
            return redirect('admin_panel')
        else:
            return HttpResponse("Invalid admin credentials")
    return render(request, 'admin_login.html')

def admin_panel(request):
    uploads = Upload.objects.all()
    return render(request, 'admin_panel.html', {'uploads': uploads})
