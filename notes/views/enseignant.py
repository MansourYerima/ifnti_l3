from notes.models import Enseignant
from notes.forms import EnseignantForm
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def enseignants(request):
    enseignants = Enseignant.objects.all()
    enseignantss = list(enseignants)
    return render(request, "notes/enseignants.html", {"enseignants": enseignantss})


def add_enseignant(request):
    form = EnseignantForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Enseignant ajoute avec succes")
    return render(request, "notes/add_eleve.html", {"form": form})

def update_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Enseignant, id=enseignant_id)

    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return HttpResponse("Enseignant modifier avec succes")
    else:
        form = EnseignantForm(instance=enseignant)

    return render(request, 'notes/update_enseignant.html', {'form': form, 'enseignant': enseignant})
