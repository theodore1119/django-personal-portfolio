from django.urls import path
from . import views

app_name = 'teaching'

urlpatterns = [
    path('', views.all_teaching, name='all_teaching'),
]