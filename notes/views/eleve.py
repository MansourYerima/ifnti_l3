from django.shortcuts import render
from django.shortcuts import get_object_or_404

from notes.models import Eleve


def eleves(request):
    eleves = Eleve.objects.all()
    elevess = list(eleves)
    return render(request, "notes/eleves.html", {"eleves":elevess})


def eleve(request, id):
    eleve = get_object_or_404(Eleve, pk=id)
    return render(request, "notes/eleve.html", {"eleve":eleve})
