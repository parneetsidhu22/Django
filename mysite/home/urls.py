
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login/', views.mylogin, name="login"),
    path('logout/', views.mylogout, name="logout"),
    path('register/', views.register, name="register")
]
