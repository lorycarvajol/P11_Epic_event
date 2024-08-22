from django.shortcuts import render, redirect
from .forms import CollaborateurForm
from .models import Collaborateur

def accueil(request):
    return render(request, 'crm/accueil.html')

def liste_collaborateurs(request):
    collaborateurs = Collaborateur.objects.all()
    return render(request, 'crm/liste_collaborateurs.html', {'collaborateurs': collaborateurs})

def ajouter_collaborateur(request):
    if request.method == 'POST':
        form = CollaborateurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_collaborateurs')
    else:
        form = CollaborateurForm()
    return render(request, 'crm/ajouter_collaborateur.html', {'form': form})
