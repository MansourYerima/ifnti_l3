from django.forms import ModelForm
from django.core.exceptions import ValidationError
from notes.models import Eleve

class EleveForm(ModelForm):
    # matieres = forms.ModelMultipleChoiceField(
    #     queryset=Matiere.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False,
    #     label="Matières de l'élève"
    # )
    class Meta:
        model = Eleve
        fields = ['nom', 'prenom', 'sexe', 'date', 'niveau', 'matieres']
        labels = {
            "nom": "Nom de l'eleve",
            "prenom": "Prenom de l'eleve",
            "sexe": "Sexe de l'eleve",
            "date": "Date de naissance de l'eleve",
            "niveau": "Niveau de l'eleve",
            "matieres": "Matieres de l'eleve",
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

    def clean(self):
        cleaned_data = super().clean()

        niveau = cleaned_data.get('niveau')
        matieres = cleaned_data.get('matieres')

        if niveau and matieres:
            for matiere in matieres:
                if not matiere.niveau.filter(id=niveau.id).exists():
                    raise ValidationError(
                        f"La matière « {matiere.nom} » ne correspond pas au niveau {niveau.nom}."
                    )
        return cleaned_data

