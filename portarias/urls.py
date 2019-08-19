from django.urls import path

from portarias import views


urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar-visitante/', views.adicionarVisitante, name='adicionar-visitante'),
    path('horarios/', views.adicionarHorarios, name='adicionar-horarios'),
]