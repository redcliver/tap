from django.shortcuts import render
from produtos.models import prod, bases, adicional

# Create your views here.
def produtos(request):
    if request.user.is_authenticated():
        return render(request, 'produtos.html', {'title':'Produtos'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def base(request):
    if request.user.is_authenticated():
        return render(request, 'bases.html', {'title':'Bases'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def add(request):
    if request.user.is_authenticated():
        return render(request, 'add.html', {'title':'Adicional'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo_add(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('nome') != None:
            nome = request.POST.get('nome')
            valor = request.POST.get('valor')
            img = request.POST.get('img')
            novo_adicional = adicional(nome=nome, preco=valor, img=img)
            novo_adicional.save()
            msg = 'Adicional adicionado com sucesso!'
            return render(request, 'novo_add.html', {'title':'Novo adicional'})
        return render(request, 'novo_add.html', {'title':'Novo adicional'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar_add(request):
    if request.user.is_authenticated():
        adds1 = adicional.objects.all().order_by('nome')
        return render(request, 'editar_add.html', {'title':'Editar adicional', 'adds1':adds1})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar_add1(request):
    if request.user.is_authenticated():
        if request.method == 'GET' and request.GET.get('add_id') != None:
            addID = request.GET.get('add_id')
            add_obj = adicional.objects.filter(id=addID).get()
            return render(request, 'editar_add1.html', {'title':'Editar adicional', 'add1':add_obj})
        elif request.method == 'POST' and request.POST.get('add_id') != None:
            addID = request.POST.get('add_id')
            nome = request.POST.get('nome')
            valor = request.POST.get('valor')
            img = request.POST.get('img')
            add_obj = adicional.objects.filter(id=addID).get()
            add_obj.nome = nome
            add_obj.preco = valor
            add_obj.img = img
            add_obj.save()
            msg = 'Adicional editado com sucesso!'
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'editar_add.html', {'title':'Editar adicional'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def nova_base(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('nome') != None:
            nome = request.POST.get('nome')
            valor = request.POST.get('valor')
            img = request.POST.get('img')
            nova_base = bases(nome=nome, preco=valor, img=img)
            nova_base.save()
            msg = 'Base adicionado com sucesso!'
            return render(request, 'nova_base.html', {'title':'Nova base'})
        return render(request, 'nova_base.html', {'title':'Nova base'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar_base(request):
    if request.user.is_authenticated():
        bases1 = bases.objects.all().order_by('nome')
        return render(request, 'editar_base.html', {'title':'Editar base', 'bases1':bases1})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar_base1(request):
    if request.user.is_authenticated():
        if request.method == 'GET' and request.GET.get('base_id') != None:
            baseId = request.GET.get('base_id')
            base_obj = bases.objects.filter(id=baseId).get()
            return render(request, 'editar_base1.html', {'title':'Editar bases', 'bas1':base_obj})
        elif request.method == 'POST' and request.POST.get('base_id') != None:
            baseId = request.POST.get('base_id')
            nome = request.POST.get('nome')
            valor = request.POST.get('valor')
            img = request.POST.get('img')
            base_obj = bases.objects.filter(id=baseId).get()
            base_obj.nome = nome
            base_obj.preco = valor
            base_obj.img = img
            base_obj.save()
            msg = 'Base editada com sucesso!'
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'editar_base.html', {'title':'Editar base'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('nome') != None:
            nome = request.POST.get('nome')
            valor = request.POST.get('valor')
            img = request.POST.get('img')
            novo_prod = prod(nome=nome, preco=valor, img=img)
            novo_prod.save()
            msg = 'Produto adicionado com sucesso!'
            return render(request, 'novo.html', {'title':'Novo Produto'})
        return render(request, 'novo.html', {'title':'Novo produtos'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar(request):
    if request.user.is_authenticated():
        pro1 = prod.objects.all().order_by('nome')
        return render(request, 'editar.html', {'title':'Editar produtos', 'pro1':pro1})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar1(request):
    if request.user.is_authenticated():
        if request.method == 'GET' and request.GET.get('prod_id') != None:
            prodId = request.GET.get('prod_id')
            prod_obj = prod.objects.filter(id=prodId).get()
            return render(request, 'editar1.html', {'title':'Editar produtos', 'produto':prod_obj})
        elif request.method == 'POST' and request.POST.get('prod_id') != None:
            prodId = request.POST.get('prod_id')
            nome = request.POST.get('nome')
            valor = request.POST.get('valor')
            img = request.POST.get('img')
            prod_obj = prod.objects.filter(id=prodId).get()
            prod_obj.nome = nome
            prod_obj.preco = valor
            prod_obj.img = img
            prod_obj.save()
            msg = 'Produto editado com sucesso!'
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'editar.html', {'title':'Editar produtos'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

