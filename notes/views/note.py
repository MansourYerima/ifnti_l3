from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from notes.models import Eleve, Matiere
from notes.forms import NoteForm

@login_required
def add_note(request, eleve_id, matiere_id):
    user = request.user
    eleve = get_object_or_404(Eleve, id=eleve_id)
    matiere = get_object_or_404(Matiere, id=matiere_id)

    if not eleve.matieres.filter(id=matiere.id).exists():
        return HttpResponse(
            f"L'élève {eleve} ne suit pas la matière {matiere.nom}."
        )

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.eleve = eleve
            note.matiere = matiere
            note.save()
            return HttpResponse(f"Note sauvegarde pour l'eleve {eleve.nom}")
    else :
        form = NoteForm()

    return render(request, "notes/add_note.html", {"form": form, "eleve": eleve, "matiere": matiere, "user": user})
