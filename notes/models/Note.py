from django.db import models
from .Eleve import Eleve
from .Matiere import Matiere
from django.core.validators import MinValueValidator, MaxValueValidator


class Note(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name="notesEleve")
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name="notesMatiere")
    valeur = models.FloatField(null=True, validators = [
        MinValueValidator(0),
        MaxValueValidator(20)
    ])

    def __str__(self):
        return f"{self.eleve.prenom} {self.eleve.nom} - {self.matiere.nom}: {self.valeur}"