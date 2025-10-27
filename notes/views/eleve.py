from django.shortcuts import render
from django.shortcuts import get_object_or_404
from notes.forms import EleveForm
from notes.models import Eleve
from django.http import HttpResponse



def eleves(request):
    eleves = Eleve.objects.all()
    elevess = list(eleves)
    return render(request, "notes/eleves.html", {"eleves":elevess})


def eleve(request, id):
    eleve = get_object_or_404(Eleve, pk=id)
    matiere_eleve = eleve.matieres.all()
    return render(request, "notes/eleve.html", {"eleve":eleve, "matieres":matiere_eleve})

def add_eleve(request):
    form = EleveForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Eleve ajoute avec succes")
    return render(request, "notes/add_eleve.html", {"form":form})

def update_eleve(request, eleve_id):
    eleve = get_object_or_404(Eleve, id=eleve_id)

    if request.method == 'POST':
        form = EleveForm(request.POST, instance=eleve)
        if form.is_valid():
            form.save()
            return HttpResponse("Eleve modifier avec succes")
    else:
        form = EleveForm(instance=eleve)

    return render(request, 'notes/update_eleve.html', {'form': form, 'eleve': eleve})

