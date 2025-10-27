from django.forms import ModelForm
from django.core.exceptions import ValidationError
from notes.models import Enseignant

class EnseignantForm(ModelForm):
    class Meta:
        model = Enseignant
        fields = "__all__"
        labels = {
            "nom": "Nom de l'enseignant",
            "prenom": "Prenom de l'enseignant",
            "sexe": "Sexe de l'enseignant",
            "date": "Date de naissance de l'enseignant",
        }

    def clean_nom(self):
        cleaned_data = super().clean()
        nom = cleaned_data.get('nom')

        if nom and not nom.isalpha():
            raise ValidationError("Le nom ne doit contenir que des lettres.")
        return nom

    def clean_prenom(self):
        cleaned_data = super().clean()
        prenom = cleaned_data.get('prenom')

        if prenom and not prenom.isalpha():
            raise ValidationError("Le prenom ne doit contenir que des lettres.")
        return prenom

