from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404


from notes.models import Matiere


def matieres(request):
    matieres = Matiere.objects.all()
    # matiere_enseignant = []
    # for matiere in matieres:
    #     matiere_enseignant.append({
    #         "matiere_id":matiere.id,
    #         "matiere":matiere.nom,
    #         "enseignant":matiere.enseignant.nom
    #     })
    #return HttpResponse(matiere_enseignant)
    return render(request, "notes/matieres.html", {"matieres":matieres})

def matiere(request, id):
    matiere = get_object_or_404(Matiere, pk=id)
    return render(request, "notes/matiere.html", {"matiere":matiere})