from django.db import models
from .Personne import Personne
from .Niveau import Niveau


class Eleve(Personne):
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE, related_name="eleves")
    matricule = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"

    def __str__(self):
        return f"{self.prenom} {self.nom}"