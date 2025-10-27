from django.db import models
from .Personne import Personne
from .Niveau import Niveau
from .Matiere import Matiere


class Eleve(Personne):
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE, related_name="eleves")
    matieres = models.ManyToManyField(Matiere, related_name='eleves', blank=True)
    matricule = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"

    def save(self, *args, **kwargs):
        annee_naissance = self.date.year
        matricule = (
                self.nom[:2].upper() +
                self.prenom[:2].upper() +
                self.sexe.upper() +
                str(annee_naissance)
        )
        self.matricule = matricule
        super().save(*args, **kwargs)

        if self.matieres.count() == 0:
            matieres_niveau = Matiere.objects.filter(niveau=self.niveau)
            #print(matieres_niveau)
            #self.matieres.set(matieres_niveau)
            #print(matieres_niveau[0].id)
            for i in matieres_niveau:
                self.matieres.add(i.id)


    def __str__(self):
        return f"{self.prenom} {self.nom}"