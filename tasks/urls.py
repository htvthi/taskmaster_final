from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.loginPage, name="logout"),
    
    path('update/<str:pk>/', views.updateTask, name="update"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    
]