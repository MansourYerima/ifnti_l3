from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Avg
from django.db.models import Count

from notes.models import Eleve, Matiere, Enseignant, Note, Niveau
from notes.views import eleves

def statistique(request):
    nbr_eleves = Eleve.objects.count()
    nbr_matieres = Matiere.objects.count()
    nbr_enseignants = Enseignant.objects.count()
    nbr_notes = Note.objects.count()

    #Moyenne generale de toutes les notes par eleves
    eleves_moyenne_gen = Eleve.objects.annotate(moyenne=Avg("notesEleve__valeur"))

    #Moyenne des notes par matiere
    matieres = Matiere.objects.annotate(moyenne=Avg("notesMatiere__valeur"))

    #Les meilleures
    meilleures = Eleve.objects.annotate(moyenne=Avg("notesEleve__valeur")).order_by("-moyenne")

    #Les niveaux
    niveaux = Niveau.objects.annotate(nombre_eleves = Count("eleves"))
    # niv = []
    # for n in niveaux:
    #     niv.append(len(n.eleves))

    return render(request, "notes/statistiques.html",{
        "eleves" : nbr_eleves,
        "matieres" : nbr_matieres,
        "enseignants" : nbr_enseignants,
        "notes" : nbr_notes,
        "moyenne_eleve" : eleves_moyenne_gen,
        "moyenne_matiere" : matieres,
        "meilleures" : meilleures,
        "niveaux" : niveaux
    })

    #return HttpResponse(eleves)