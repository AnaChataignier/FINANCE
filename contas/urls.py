from django.urls import path
from . import views

urlpatterns = [
    path('definir_contas/', views.definir_contas, name="definir_contas"),
    path('deletar_conta_mensal/<int:id>', views.deletar_conta_mensal, name="deletar_conta_mensal"),  
]