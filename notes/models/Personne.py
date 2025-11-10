from django.db import models
from django.contrib.auth.models import User



class Personne(models.Model):
    SEXES = {
        "M":"Masculin",
        "F":"Feminin",
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1, choices=SEXES)
    date = models.DateField()

    class Meta:
        abstract = True