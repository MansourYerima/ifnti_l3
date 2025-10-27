from django.contrib import admin
from .models import Niveau, Eleve, Enseignant, Matiere, Note
from .forms import EleveForm

# Register your models here.
admin.site.register(Niveau)
admin.site.register(Enseignant)
admin.site.register(Matiere)
admin.site.register(Note)

class EleveAdmin(admin.ModelAdmin):
    form = EleveForm

admin.site.register(Eleve, EleveAdmin)
