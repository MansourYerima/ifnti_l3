from django.db import models
from .Eleve import Eleve
from .Matiere import Matiere


class Note(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name="notesEleve")
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name="notesMatiere")
    valeur = models.FloatField(null=True)

    def __str__(self):
        return f"{self.eleve.prenom} {self.eleve.nom} - {self.matiere.nom}: {self.valeur}"