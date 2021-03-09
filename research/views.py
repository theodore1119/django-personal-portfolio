from django.shortcuts import render
from .models import Research

def all_research(request):
    researchs = Research.objects.all()
    return render(request, 'research/all_research.html', {'researchs':researchs})
