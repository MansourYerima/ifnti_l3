from django.urls import path
from . import views
app_name = "notes"
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('statistiques/', views.statistique, name='statistique'),
    path('eleves/', views.eleves, name='eleves'),
    path('eleve/<int:id>/', views.eleve, name='eleve'),
    path('enseignant/<int:id>/', views.enseignant, name='enseignant'),
    path('matieres/', views.matieres, name='matieres'),
    path('matiere/<int:id>/', views.matiere, name='matiere'),
    path('niveau/<int:id>/', views.niveau, name='niveau'),
    path('ajouter_note/<int:eleve_id>/<int:matiere_id>/', views.add_note, name='add_note'),
    path('ajouter_eleve/', views.add_eleve, name='add_eleve'),
    path('ajouter_enseignant/', views.add_enseignant, name='add_enseignant'),
    path('modifier_eleve/<int:eleve_id>', views.update_eleve, name='update_eleve'),
    path('modifier_enseignant/<int:enseignant_id>', views.update_enseignant, name='update_enseignant'),
    path('enseignants/', views.enseignants, name='enseignants')
]

