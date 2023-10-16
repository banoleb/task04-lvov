from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.redir, name='redir'),
    path('app/', views.showall, name='index'),
]