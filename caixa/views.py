from django.shortcuts import render
from .models import caixa_geral
from decimal import *
from datetime import datetime, timedelta

# Create your views here.
def caixa(request):
    if request.user.is_authenticated():
        try:
            caixa = caixa_geral.objects.latest('id')
            total = caixa.total
        except:
            caixa = caixa_geral(tipo=1, total=0, desc="abertura")
            caixa.save()
            total = caixa.total
        entrada = caixa_geral.objects.filter(tipo=1).count()
        saida = caixa_geral.objects.filter(tipo=2).count()
        return render(request, 'caixa.html', {'title':'Caixa', 'total':total, 'entrada':entrada, 'saida':saida})
        return render(request, 'caixa.html', {'title':'Caixa'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def entrada(request):
    if request.user.is_authenticated():
        try:
            caixa = caixa_geral.objects.latest('id')
            total = caixa.total
        except:
            caixa = caixa_geral(tipo=1, total=0, desc="abertura")
            caixa.save()
            total = caixa.total
        if request.method == 'POST' and request.POST.get('entrada') != None:
            valor_ret = request.POST.get('entrada')
            desc = request.POST.get('motivo')
            total = caixa.total + Decimal(valor_ret)
            nova_op = caixa_geral(total=total, tipo=1, desc=desc)
            nova_op.save()
            msg = "Entrada registrada com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'entrada.html', {'title':'Entrada', 'total':total})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def retirada(request):
    if request.user.is_authenticated():
        try:
            caixa = caixa_geral.objects.latest('id')
            total = caixa.total
        except:
            caixa = caixa_geral(tipo=1, total=0, desc="abertura")
            caixa.save()
            total = caixa.total
        if request.method == 'POST' and request.POST.get('retirada') != None:
            valor_ret = request.POST.get('retirada')
            desc = request.POST.get('motivo')
            total = caixa.total - Decimal(valor_ret)
            nova_op = caixa_geral(total=total, tipo=2, desc=desc)
            nova_op.save()
            msg = "Retirada concluida com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'retirada.html', {'title':'Retirada' , 'total':total})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def fechar(request):
    if request.user.is_authenticated():
        try:
            caixa = caixa_geral.objects.latest('id')
            total = caixa.total
        except:
            caixa = caixa_geral(tipo=1, total=0, desc="abertura")
            caixa.save()
            total = caixa.total
        if request.method == 'POST' and request.POST.get('retirada') != None:
            valor_ret = request.POST.get('retirada')
            total = caixa.total - Decimal(valor_ret)
            desc = "Fechamento, R$-"+str(valor_ret)+""            
            nova_op = caixa_geral(total=total, tipo=2, desc=desc)
            nova_op.save()
            msg = "Fechamento concluído com sucesso, total em caixa R$ "+str(total)+""
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'fechar.html', {'title':'Fechar caixa', 'total':total})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})