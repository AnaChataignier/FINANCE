from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categoria, Conta
from django.contrib import messages
from django.contrib.messages import constants
from .utils import calcula_total, calcula_equilibrio_financeiro
from extrato.models import Valores
from datetime import datetime
from contas.models import ContaPagar


def home(request):
    valores = Valores.objects.filter(data__month = datetime.now().month )
    entradas = valores.filter(tipo='E')
    saida = valores.filter(tipo='S')
    contas = Conta.objects.all()
    saldo_total = calcula_total(contas, 'valor')
    total_entradas = calcula_total(entradas, 'valor')
    total_saidas = calcula_total(saida, 'valor')
    percentual_gastos_essenciais, percentual_gastos_nao_essenciais  = calcula_equilibrio_financeiro()
    contas_mensais = ContaPagar.objects.all()
    total_mensal=0
    for valor in contas_mensais:
        total_mensal += valor.valor
        
    total_livre = total_entradas - total_mensal + total_saidas
    
    return render(request, 'home.html', {'contas': contas, 'saldo_total' : saldo_total,'total_entradas':total_entradas, 'total_saidas':total_saidas, 'percentual_gastos_essenciais': int(percentual_gastos_essenciais), 'percentual_gastos_nao_essenciais': int(percentual_gastos_nao_essenciais), 'total_mensal': total_mensal, 'total_livre': total_livre})


def gerenciar(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    saldo_total = calcula_total(contas, 'valor')
    
    return render(request, 'gerenciar.html', {'contas': contas, 'saldo_total':saldo_total, 'categorias':categorias})

def cadastrar_banco(request):
    contas = Conta.objects.all()
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
    
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('/gerenciar/')
    
    conta = Conta(
        apelido = apelido,
        banco=banco,
        tipo=tipo,
        valor=valor,
        icone=icone
    )

    conta.save()
    messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso')
    return redirect('/gerenciar/')

def deletar_banco(request, id):
    conta = Conta.objects.get(id=id)
    conta.delete()
    
    messages.add_message(request, constants.SUCCESS, 'Conta removida com sucesso')
    return redirect('/gerenciar/')

def deletar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    
    messages.add_message(request, constants.SUCCESS, 'Conta removida com sucesso')
    return redirect('/gerenciar/')
    


def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))

    categoria = Categoria(
        categoria=nome,
        essencial=essencial
    )

    categoria.save()

    messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso')
    return redirect('/gerenciar/')

def update_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    categoria.essencial = not categoria.essencial

    categoria.save()

    return redirect('/gerenciar/')


    