from django.db import models
from .Enseignant import Enseignant
from .Niveau import Niveau


class Matiere(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name="matieres")
    #eleve = models.ManyToManyField(Eleve, related_name='matieres', blank=True)
    niveau = models.ManyToManyField(Niveau, related_name='matieres')
    nom = models.CharField(unique=True)

    class Meta:
        verbose_name = "Matiere"
        verbose_name_plural = "Matieres"

    def __str__(self):
        return self.nom