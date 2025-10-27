from django.forms import ModelForm
from notes.models import Note

class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ['valeur']
        labels = {
            "valeur":"Note sur 20"
        }

