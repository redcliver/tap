from django.db import models

# Create your models here.
class prod(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class prod_item(models.Model):
    id = models.AutoField(primary_key=True)
    produto = models.ForeignKey(prod)
    qnt = models.IntegerField()
    total = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)

class bases(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class adicional(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.nome

class montar_item(models.Model):
    id = models.AutoField(primary_key=True)
    base1 = models.ManyToManyField(bases)
    ads1 = models.ManyToManyField(adicional)
    total = models.DecimalField(max_digits=5, decimal_places=2, default='0')
    def __str__(self):
        return str(self.id)


class comanda(models.Model):
    id = models.AutoField(primary_key=True)
    produtos = models.ManyToManyField(prod_item)
    montados = models.ManyToManyField(montar_item)
    pagamento = models.CharField(max_length=100, null=True, blank=True)
    total = models.DecimalField(max_digits=5, decimal_places=2, default='0')
    
    def __str__(self):
        return str(self.id)

