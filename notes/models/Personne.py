from django.db import models


class Personne(models.Model):
    SEXES = {
        "M":"Masculin",
        "F":"Feminin",
    }
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1, choices=SEXES)
    date = models.DateField()

    class Meta:
        abstract = True