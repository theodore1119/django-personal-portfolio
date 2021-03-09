from django.shortcuts import render
from .models import Teaching

def all_teaching(request):
    teachings = Teaching.objects.all()
    return render(request, 'teaching/all_teaching.html', {'teachings':teachings})