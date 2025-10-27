from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from notes.models import Niveau, Enseignant, Matiere, Eleve, Note
import random


fake = Faker("fr_FR")


class Command(BaseCommand):
    help = "Seed initial data for the school system"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("🔄 Initialisation des données..."))

        # 1️⃣ Créer les niveaux
        niveaux = []
        for nom in ["L1", "L2", "L3"]:
            niveau, created = Niveau.objects.get_or_create(nom=nom)
            niveaux.append(niveau)
        self.stdout.write(self.style.SUCCESS("✅ Niveaux créés."))

        # 2️⃣ Créer les enseignants
        enseignants = []
        for _ in range(5):
            enseignant = Enseignant.objects.create(
                nom=fake.last_name(),
                prenom=fake.first_name(),
                sexe=random.choice(["M", "F"]),
                email=fake.email(),
                date=fake.date_of_birth(minimum_age=25, maximum_age=50),
            )
            enseignants.append(enseignant)
        self.stdout.write(self.style.SUCCESS("✅ Enseignants créés."))

        # 3️⃣ Créer les matières et les associer aux niveaux
        noms_matieres = ["Mathématiques", "Physique", "Informatique", "Anglais", "Droit", "Économie"]
        matieres = []
        for nom in noms_matieres:
            enseignant = random.choice(enseignants)
            matiere, created = Matiere.objects.get_or_create(
                nom=nom,
                enseignant=enseignant,
            )
            # Associer à un ou plusieurs niveaux
            niveaux_associes = random.sample(niveaux, k=random.randint(1, 3))
            matiere.niveau.set(niveaux_associes)
            matiere.save()
            matieres.append(matiere)
        self.stdout.write(self.style.SUCCESS("✅ Matières créées et liées aux niveaux."))

        # 4️⃣ Créer les élèves
        for i in range(10):
            niveau = random.choice(niveaux)
            eleve = Eleve.objects.create(
                nom=fake.last_name(),
                prenom=fake.first_name(),
                sexe=random.choice(["M", "F"]),
                email=fake.email(),
                date=fake.date_of_birth(minimum_age=18, maximum_age=25),
                niveau=niveau,
            )
            # Le `save()` ajoute déjà les matières automatiquement
        self.stdout.write(self.style.SUCCESS("✅ Élèves créés avec leurs matières."))

        # 5️⃣ Créer des notes pour chaque élève et matière correspondante
        for eleve in Eleve.objects.all():
            for matiere in eleve.matieres.all():
                Note.objects.create(
                    eleve=eleve,
                    matiere=matiere,
                    valeur=random.uniform(8, 18)
                )
        self.stdout.write(self.style.SUCCESS("✅ Notes générées pour chaque élève."))

        self.stdout.write(self.style.SUCCESS("🎉 Données de test insérées avec succès !"))
