from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        return render(request, 'home/home.html', {'title':'Home'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def outros(request):
    if request.user.is_authenticated():
        return render(request, 'home/outros.html', {'title':'Outros'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})