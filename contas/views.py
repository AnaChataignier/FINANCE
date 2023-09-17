from django.shortcuts import render, redirect
from perfil.models import Categoria, Conta
from .models import ContaPagar, ContaPaga
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime

def definir_contas(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        contas_mensais = ContaPagar.objects.all()
        return render(request, 'definir_contas.html', {'categorias': categorias, 'contas_mensais': contas_mensais })
    else:
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        dia_pagamento = request.POST.get('dia_pagamento')
        
        conta = ContaPagar(
            titulo = titulo,
            categoria_id = categoria,
            descricao = descricao,
            valor=valor,
            dia_pagamento=dia_pagamento
            
            
        )
        conta.save()
        
        messages.add_message(request, constants.SUCCESS, 'Conta Cadastrada com sucesso')
        return redirect('/contas/definir_contas')
        

       
        
def deletar_conta_mensal(request, id):
    conta_mensal = ContaPagar.objects.get(id=id)
    conta_mensal.delete()
    
    messages.add_message(request, constants.SUCCESS, 'Conta mensal removida com sucesso')
    return redirect('definir_contas')


    
    
     
    