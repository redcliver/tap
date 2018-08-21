from django.shortcuts import render
from contas.models import conta
from django.utils import timezone
# Create your views here.
def home(request):
    if request.user.is_authenticated():
        try:
            hoje = timezone.now().strftime("Y-m-d")
            contagem = 0
            for c in conta.objetas.filter(estado=1):
                if c.data_venc <= hoje:
                    contagem = contagem + 1
        except:
            contagem = 0
        return render(request, 'home/home.html', {'title':'Home','contagem':contagem})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def outros(request):
    if request.user.is_authenticated():
        return render(request, 'home/outros.html', {'title':'Outros'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})