from django.urls import path
from app_cadastro import views

urlpatterns = [
    # route, responsible view, reference name
    # users.com
    path('', views.home, name='home'),

    # users.com/users
    path('users/', views.users, name='users_list')
]
