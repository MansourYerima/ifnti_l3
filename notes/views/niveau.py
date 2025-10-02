from django.shortcuts import get_object_or_404
from django.shortcuts import render


from notes.models import Niveau


def niveau(request, id):
    niveau = get_object_or_404( Niveau ,pk = id)
    return render(request, "notes/niveau.html", {"niveau":niveau})