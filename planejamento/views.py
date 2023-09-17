from django.shortcuts import render, redirect
from perfil.models import Categoria, Conta
from extrato.models import Valores
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'definir_planejamento.html', {'categorias': categorias})

@csrf_exempt
def update_valor_categoria(request, id):
    novo_valor = json.load(request)['novo_valor']
    categoria = Categoria.objects.get(id=id)
    categoria.valor_planejamento = novo_valor
    categoria.save()

    return JsonResponse({'status': 'Sucesso'})

def ver_planejamento(request):
    categorias = Categoria.objects.all()
    
    total_planejado = 0
    for categoria in categorias:
        total_planejado += categoria.valor_planejamento 
        
    valor_total = Valores.objects.filter(tipo = 'S')
    gasto_geral = 0
    for valor in valor_total:
        gasto_geral += valor.valor
    
    percentual_gastos = int((gasto_geral*100) / total_planejado)
     
    return render(request, 'ver_planejamento.html', {'categorias': categorias, 'gasto_geral' : gasto_geral, 'total_planejado': total_planejado, 'percentual_gastos':percentual_gastos})