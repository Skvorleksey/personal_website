from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def cv(request):
    jobs = models.WorkExperienceEntry.objects.order_by('-start')
    skills = models.Skill.objects.all()
    context = {
        'jobs': jobs,
        'skills': skills,
    }
    return render(request, 'main/cv.html', context=context)


def interaction(request):
    return render(request, 'main/interaction.html')
