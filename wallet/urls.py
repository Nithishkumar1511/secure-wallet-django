from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_file, name='upload'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-login/', views.admin_login, name='admin_login'),
]
