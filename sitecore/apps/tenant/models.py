from django.db import models

class Tenant(models.Model):
    nome = models.CharField(max_length=255)
    subdominio = models.CharField(max_length=255, unique=True)  # Cada tenant tem um subdomínio único
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Loja(models.Model):
    tenant = models.OneToOneField(Tenant, on_delete=models.CASCADE, related_name='lojas_tenant')  # Cada tenant tem uma única loja
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)  # Produto vinculado à loja
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
