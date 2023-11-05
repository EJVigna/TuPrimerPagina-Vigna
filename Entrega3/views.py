from django.shortcuts import render, redirect
from PrimerWeb import models



def padre (request):
    return render(request, 'padre.html')
