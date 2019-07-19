from django.urls import path
from wolforhusky import views

urlpatterns = [
    path('', views.index, name='index'),
]