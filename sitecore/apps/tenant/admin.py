from django.contrib import admin
from .models import Tenant, Loja, Produto

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('nome', 'subdominio', 'data_criacao')
    search_fields = ('nome', 'subdominio')

@admin.register(Loja)
class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tenant')
    search_fields = ('nome',)
    list_filter = ('tenant',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'loja')
    search_fields = ('nome',)
    list_filter = ('loja',)
