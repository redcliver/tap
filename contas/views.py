# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import conta
from caixa.models import caixa_geral
from django.shortcuts import render
from decimal import Decimal

# Create your views here.
def contas(request):
    if request.user.is_authenticated():
        return render(request, 'contas.html', {'title':'Contas'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def nova_conta(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            nome = request.POST.get('nome')
            valor = request.POST.get('valor')
            data_venc = request.POST.get('data_venc')
            desc = request.POST.get('desc')
            nova_cont = conta(nome=nome, valor=valor, data_venc=data_venc, desc=desc)
            nova_cont.save()
            msg = "Conta adicionada com sucesso!"
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'nova_conta.html', {'title':'Nova Contas'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar_conta(request):
    if request.user.is_authenticated():
        conts = conta.objects.all().order_by('data_venc')
        if request.method == 'GET' and request.GET.get('cont_id') != None:
            cont_id = request.GET.get('cont_id')
            cont = conta.objects.filter(id=cont_id).get()
            return render(request, 'editar_conta1.html', {'title':'Editar Conta', 'cont':cont})
        return render(request, 'editar_conta.html', {'title':'Editar Conta', 'conts':conts})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar_conta1(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            cont_id = request.POST.get('cont_id')
            cont_obj = conta.objects.filter(id=cont_id).get()
            nome = request.POST.get('nome')
            valor = request.POST.get('valor')
            data_venc = request.POST.get('data_venc')
            desc = request.POST.get('desc')
            cont_obj.nome = nome
            cont_obj.valor = valor
            cont_obj.data_venc = data_venc
            cont_obj.desc = desc
            cont_obj.save()
            msg = "conta editada com sucesso!"
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def pagar(request):
    if request.user.is_authenticated():
        conts = conta.objects.filter(estado=1).all().order_by('data_venc')
        if request.method == 'POST' and request.POST.get('cont_id') != None:
            cont_id = request.POST.get('cont_id')
            cont_obj = conta.objects.filter(id=cont_id).get()
            cont_obj.estado = 2
            cont_obj.save()
            caixa_final = caixa_geral.objects.latest('id')
            total = caixa_final.total - cont_obj.valor
            desc = "Pagamento "+ cont_obj.nome +", R$"+str(cont_obj.valor)+""
            novo_cx = caixa_geral(tipo=2, total=total, desc=desc)
            novo_cx.save()
            msg = "Conta paga com sucesso, total em caixa: R$"+ str(novo_cx.total) +""
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'pag_conta.html', {'title':'Pagar Conta', 'conts':conts})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})