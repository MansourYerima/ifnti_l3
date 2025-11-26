from django.shortcuts import render

def jpl_view(request):
    return render(request, 'notes/jpl.html')