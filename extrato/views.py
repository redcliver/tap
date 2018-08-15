from django.shortcuts import render
from caixa.models import caixa_geral
from django.utils import timezone

# Create your views here.
def extrato(request):
    if request.user.is_authenticated():
        return render(request, 'extrato.html', {'title':'Extrato'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def diario(request):
    if request.user.is_authenticated():
        now = timezone.now().strftime('%d')
        caixas = caixa_geral.objects.filter(data__day=now).all()
        return render(request, 'diario.html', {'title':'Extrato diario', 'caixas':caixas})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})