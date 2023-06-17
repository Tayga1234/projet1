from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Video_form
from .models import Video

def index(request):
    all_video = Video.objects.all()
    if request.method == "POST":
        form = Video_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige vers la page d'accueil après l'upload réussi
    else:
        form = Video_form()
    
    return render(request, 'index.html', {"form": form, "all": all_video})