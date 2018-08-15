from django.shortcuts import render
from produtos.models import prod, comanda, prod_item, bases, adicional, montar_item
from caixa.models import caixa_geral
from decimal import Decimal

# Create your views here.
def pedidos(request):
    if request.user.is_authenticated():
        if request.GET.get('cmd_id') == '' or request.GET.get('cmd_id') == None:
            cmd_id = request.GET.get('cmd_id')
            return render(request, 'pedidos.html', {'title':'Pedidos', 'cmd_id':cmd_id})
        elif request.GET.get('cmd_id') != '' or request.GET.get('cmd_id') != None:
            cmd_id = request.GET.get('cmd_id')
            return render(request, 'pedidos.html', {'title':'Pedidos', 'cmd_id':cmd_id})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def combinados(request):
    if request.user.is_authenticated():
        try:
            cmd_id = request.GET.get('cmd_id')
            return render(request, 'combinados.html', {'title':'Combinados', 'cmd_id':cmd_id})
        except:
            cmd_id = None
            return render(request, 'combinados.html', {'title':'Combinados', 'cmd_id':cmd_id})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def montar(request):
    if request.user.is_authenticated():
        if request.GET.get('cmd_id') == 'None' or request.GET.get('cmd_id') == None or request.GET.get('cmd_id') == '':
            adds1 = adicional.objects.all().order_by('nome')
            bases1 = bases.objects.all().order_by('nome')
            if request.method == 'POST':
                bas1 = request.POST.getlist('base')
                if bas1 == []:
                    bas1 = None
                ad1 = request.POST.getlist('adicional')
                if ad1 == []:
                    ad1 = None
                
                if bas1 != None and ad1 == None:
                    novo_mont = montar_item(total=0)
                    novo_mont.save()
                    for bs in bas1:
                        bas_id = int(bs)
                        bas_obj = bases.objects.filter(id=bas_id).get()
                        novo_mont.base1.add(bas_obj)
                        novo_mont.total = bas_obj.preco
                        novo_mont.save()
                        m_bs = novo_mont.base1.all()
                    mont_id = novo_mont.id
                    total_mont = novo_mont.total
                    return render(request, 'montar1.html', {'title':'Montar', 'm_bs':m_bs, 'mont_id':mont_id, 'mont_id':mont_id, 'total_mont':total_mont})
                elif ad1 != None and bas1 == None:
                    novo_mont = montar_item(total=0)
                    novo_mont.save()
                    for ad in ad1:
                        add_id = ad
                        add_id = int(ad)
                        add_obj = adicional.objects.filter(id=add_id).get()
                        novo_mont.ads1.add(add_obj)
                        novo_mont.total = add_obj.preco
                        novo_mont.save()
                        m_ad = novo_mont.ads1.all()
                    mont_id = novo_mont.id
                    total_mont = novo_mont.total
                    return render(request, 'montar1.html', {'title':'Montar', 'm_ad':m_ad, 'mont_id':mont_id, 'mont_id':mont_id, 'total_mont':total_mont})
                elif ad1 != None and bas1 != None:
                    novo_mont = montar_item(total=0)
                    novo_mont.save()
                    for ad in ad1:
                        add_id = ad
                        add_id = int(ad)
                        add_obj = adicional.objects.filter(id=add_id).get()
                        novo_mont.ads1.add(add_obj)
                        novo_mont.total = novo_mont.total + add_obj.preco
                        novo_mont.save()
                        m_ad = novo_mont.ads1.all()
                    for bs in bas1:
                        bas_id = int(bs)
                        bas_obj = bases.objects.filter(id=bas_id).get()
                        novo_mont.base1.add(bas_obj)
                        novo_mont.total = novo_mont.total + bas_obj.preco
                        novo_mont.save()
                        m_bs = novo_mont.base1.all()
                    mont_id = novo_mont.id
                    total_mont = novo_mont.total
                    return render(request, 'montar1.html', {'title':'Montar', 'm_ad':m_ad, 'm_bs':m_bs, 'mont_id':mont_id, 'total_mont':total_mont})
            return render(request, 'montar.html', {'title':'Montar', 'adds1':adds1, 'bases1':bases1})
        elif request.GET.get('cmd_id') != 'None' or request.GET.get('cmd_id') != None or request.GET.get('cmd_id') != '':
            cmd_id = request.GET.get('cmd_id')
            cmd_obj = comanda.objects.filter(id=cmd_id).get()
            adds1 = adicional.objects.all().order_by('nome')
            bases1 = bases.objects.all().order_by('nome')
            if request.method == 'POST':
                bas1 = request.POST.getlist('base')
                if bas1 == []:
                    bas1 = None
                ad1 = request.POST.getlist('adicional')
                if ad1 == []:
                    ad1 = None
                
                if bas1 != None and ad1 == None:
                    novo_mont = montar_item(total=0)
                    novo_mont.save()
                    for bs in bas1:
                        bas_id = int(bs)
                        bas_obj = bases.objects.filter(id=bas_id).get()
                        novo_mont.base1.add(bas_obj)
                        novo_mont.total = bas_obj.preco
                        novo_mont.save()
                        m_bs = novo_mont.base1.all()
                    mont_id = novo_mont.id
                    total_mont = novo_mont.total
                    return render(request, 'montar1.html', {'title':'Montar', 'm_bs':m_bs, 'mont_id':mont_id, 'mont_id':mont_id, 'cmd_id':cmd_id, 'total_mont':total_mont})
                elif ad1 != None and bas1 == None:
                    novo_mont = montar_item(total=0)
                    novo_mont.save()
                    for ad in ad1:
                        add_id = ad
                        add_id = int(ad)
                        add_obj = adicional.objects.filter(id=add_id).get()
                        novo_mont.ads1.add(add_obj)
                        novo_mont.total = add_obj.preco
                        novo_mont.save()
                        m_ad = novo_mont.ads1.all()
                    mont_id = novo_mont.id
                    total_mont = novo_mont.total
                    return render(request, 'montar1.html', {'title':'Montar', 'm_ad':m_ad, 'mont_id':mont_id, 'mont_id':mont_id, 'cmd_id':cmd_id, 'total_mont':total_mont})
                elif ad1 != None and bas1 != None:
                    novo_mont = montar_item(total=0)
                    novo_mont.save()
                    for ad in ad1:
                        add_id = ad
                        add_id = int(ad)
                        add_obj = adicional.objects.filter(id=add_id).get()
                        novo_mont.ads1.add(add_obj)
                        novo_mont.total = novo_mont.total + add_obj.preco
                        novo_mont.save()
                        m_ad = novo_mont.ads1.all()
                    for bs in bas1:
                        bas_id = int(bs)
                        bas_obj = bases.objects.filter(id=bas_id).get()
                        novo_mont.base1.add(bas_obj)
                        novo_mont.total = novo_mont.total + bas_obj.preco
                        novo_mont.save()
                        m_bs = novo_mont.base1.all()
                    mont_id = novo_mont.id
                    total_mont = novo_mont.total
                    return render(request, 'montar1.html', {'title':'Montar', 'm_ad':m_ad, 'm_bs':m_bs, 'mont_id':mont_id, 'cmd_id':cmd_id, 'total_mont':total_mont})
            return render(request, 'montar.html', {'title':'Montar', 'adds1':adds1, 'bases1':bases1, 'cmd_id':cmd_id})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

    
def montar1(request):
    if request.user.is_authenticated():
        try:
            mon_id = request.POST.get('mont_id')
            mont_obj = montar_item.objects.filter(id=mon_id).get()
        except:
            mont_obj = None

        if request.POST.get('cmd_id') == 'None' or request.POST.get('cmd_id') == None or request.POST.get('cmd_id') == '':
            if mont_obj != None:
                nova_cmd = comanda(total=mont_obj.total)
                nova_cmd.save()
                nova_cmd.montados.add(mont_obj)
                nova_cmd.save()
                cmd_id = nova_cmd.id
                prods1 = nova_cmd.produtos.all()
                monts1 = nova_cmd.montados.all()
                cmd_total = nova_cmd.total
            return render(request, 'finalizar.html', {'title':'Finalizar', 'cmd_id':cmd_id, 'prods1':prods1, 'monts1':monts1, 'cmd_total':cmd_total})
        elif request.POST.get('cmd_id') != 'None' or request.POST.get('cmd_id') != None or request.POST.get('cmd_id') != '':
            cmd_id = request.POST.get('cmd_id')
            cmd_obj = comanda.objects.filter(id=cmd_id).get()
            if mont_obj != None:
                cmd_obj.montados.add(mont_obj)
                cmd_id = cmd_obj.id
                cmd_total = cmd_obj.total + mont_obj.total
                cmd_obj.total = cmd_total
                cmd_obj.save()
                prods1 = cmd_obj.produtos.all()
                monts1 = cmd_obj.montados.all()
            return render(request, 'finalizar.html', {'title':'Finalizar', 'cmd_id':cmd_id, 'prods1':prods1, 'monts1':monts1, 'cmd_total':cmd_total})

    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def bebidas(request):
    if request.user.is_authenticated():
        try:
            cmd_id = request.GET.get('cmd_id')
            return render(request, 'bebidas.html', {'title':'Bebidas', 'cmd_id':cmd_id})
        except:
            cmd_id = None
            return render(request, 'bebidas.html', {'title':'Bebidas', 'cmd_id':cmd_id})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def finalizar(request):
    if request.user.is_authenticated():
        if request.POST.get('cmd_id') == 'None' or request.POST.get('cmd_id') == None or request.POST.get('cmd_id') == '':

            try:
                prod_id = request.POST.get('comb')
                prod_obj = prod.objects.filter(img=prod_id).get()
            except:
                prod_obj = None

            try:
                beb_id = request.POST.get('bebida')
                beb_obj = prod.objects.filter(img=beb_id).get()
            except:
                beb_obj = None

            try:
                mon_id = request.POST.get('mont_id')
                mont_obj = montar_item.objects.filter(id=mon_id).get()
            except:
                mont_obj = None

            if prod_obj != None:
                novo_prod_obj = prod_item(total=prod_obj.preco, qnt=1, produto=prod_obj)
                novo_prod_obj.save()

                nova_cmd = comanda(total=prod_obj.preco)
                nova_cmd.save()
                nova_cmd.produtos.add(novo_prod_obj)
                nova_cmd.save()
                cmd_id = nova_cmd.id
                prods1 = nova_cmd.produtos.all()
                monts1 = nova_cmd.montados.all()
                cmd_total = nova_cmd.total
            elif beb_obj != None:
                novo_bebi_obj = prod_item(total=beb_obj.preco, qnt=1, produto=beb_obj)
                novo_bebi_obj.save()

                nova_cmd = comanda(total=beb_obj.preco)
                nova_cmd.save()
                nova_cmd.produtos.add(novo_bebi_obj)
                nova_cmd.save()
                cmd_id = nova_cmd.id
                prods1 = nova_cmd.produtos.all()
                monts1 = nova_cmd.montados.all()
                cmd_total = nova_cmd.total
            
            return render(request, 'finalizar.html', {'title':'Finalizar', 'cmd_id':cmd_id, 'prods1':prods1, 'cmd_total':cmd_total})
            
        elif request.POST.get('cmd_id') != 'None' or request.POST.get('cmd_id') != None or request.POST.get('cmd_id') != '':
            cmd_id = request.POST.get('cmd_id')
            cmd_obj = comanda.objects.filter(id=cmd_id).get()
            try:
                prod_id = request.POST.get('comb')
                prod_obj = prod.objects.filter(id=prod_id).get()
            except:
                prod_obj = None

            try:
                beb_id = request.POST.get('bebida')
                beb_obj = prod.objects.filter(img=beb_id).get()
            except:
                beb_obj = None

            try:
                mont_id = request.POST.get('mont_id')
                mont_obj = montar_item.objects.filter(id=mont_id).get()
            except:
                mont_obj = None

            if prod_obj != None:
                novo_prod_obj = prod_item(total=prod_obj.preco, qnt=1, produto=prod_obj)
                novo_prod_obj.save()
                cmd_total = cmd_obj.total + prod_obj.preco
                cmd_obj.total = cmd_total
                cmd_obj.produtos.add(novo_prod_obj)
                cmd_obj.save()
                cmd_id = cmd_obj.id
                cmd_total = cmd_obj.total
                prods1 = cmd_obj.produtos.all()
                monts1 = cmd_obj.montados.all()
            elif beb_obj != None:
                novo_bebi_obj = prod_item(total=beb_obj.preco, qnt=1, produto=beb_obj)
                novo_bebi_obj.save()
                cmd_total = cmd_obj.total + beb_obj.preco
                cmd_obj.total = cmd_total
                cmd_obj.produtos.add(novo_bebi_obj)
                cmd_obj.save()
                cmd_id = cmd_obj.id
                cmd_total = cmd_obj.total
                prods1 = cmd_obj.produtos.all()
                monts1 = cmd_obj.montados.all()
            
            return render(request, 'finalizar.html', {'title':'Finalizar', 'cmd_id':cmd_id, 'prods1':prods1, 'monts1':monts1, 'cmd_total':cmd_total})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def pagamento(request):
    if request.user.is_authenticated():
        cmd_id = request.GET.get('cmd_id')
        cmd_obj = comanda.objects.filter(id=cmd_id).get()
        return render(request, 'pagamento.html', {'title':'Pagamento', 'cmd_obj':cmd_obj})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def dinheiro(request):
    if request.user.is_authenticated():
        cmd_id = request.GET.get('cmd_id')
        cmd_obj = comanda.objects.filter(id=cmd_id).get()
        if request.POST.get('recebido') != None:
            rec = request.POST.get('recebido')
            cmd_id = request.POST.get('cmd_id')
            cmd_obj = comanda.objects.filter(id=cmd_id).get()
            cmd_obj.pagamento = "Dinheiro"
            cmd_obj.save()
            descri = "Comanda n "+ str(cmd_obj.id) +"."
            ultimo_cx = caixa_geral.objects.latest('id')
            total_cx = ultimo_cx.total + cmd_obj.total
            add_cx = caixa_geral(tipo=1, total=total_cx, desc=descri)
            add_cx.save()
            troco =  Decimal(rec) - cmd_obj.total 
            return render(request, 'dinheiro1.html', {'title':'Pagamento em dinheiro', 'cmd_obj':cmd_obj, 'rec':rec, 'troco':troco})
        return render(request, 'dinheiro.html', {'title':'Pagamento em dinheiro', 'cmd_obj':cmd_obj})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def cartao(request):
    if request.user.is_authenticated():
        cmd_id = request.GET.get('cmd_id')
        cmd_obj = comanda.objects.filter(id=cmd_id).get()
        cmd_obj.pagamento = "Cartao"
        cmd_obj.save()
        descri = "Comanda n "+ str(cmd_obj.id) +"."
        ultimo_cx = caixa_geral.objects.latest('id')
        total_cx = ultimo_cx.total + cmd_obj.total
        add_cx = caixa_geral(tipo=1, total=total_cx, desc=descri)
        add_cx.save()
        msg = "Pedido concluido com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def final(request):
    if request.user.is_authenticated():
        msg = "Pedido concluido com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})