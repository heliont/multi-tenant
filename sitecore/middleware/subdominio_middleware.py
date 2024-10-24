# middleware/subdominio.py

# middleware/subdominio.py

# middleware/subdominio.py

# middleware/subdominio.py

from django.shortcuts import render
from tenant.models import Loja, Tenant

class SubdominioMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split('.')

        # Ignorar a verificação de loja para superusuários
        if request.user.is_superuser:
            return self.get_response(request)

        # Tratamento para o admin no subdomínio 'app.booksite.com.br'
        if len(host) > 2 and host[0] == 'app' and host[1] == 'booksite' and host[2] == 'com.br':
            if request.path.startswith('/admin/') or request.path.startswith('/'):
                return self.get_response(request)
            return self.render_subdominio_invalido(request)

        # Verifica se há um subdomínio e trata o isolamento de dados do Tenant
        if len(host) > 2:
            subdominio = host[0]  # Captura o subdomínio
            try:
                request.loja = Loja.objects.get(tenant__subdominio=subdominio)  # Busca a loja pelo subdomínio
            except Loja.DoesNotExist:
                return self.render_subdominio_invalido(request)
            except Tenant.DoesNotExist:
                return self.render_subdominio_invalido(request)
        else:
            request.loja = None # Não há subdomínio, ou seja, é um domínio inválido

        return self.get_response(request)

    def render_subdominio_invalido(self, request):
        """Renderiza um template quando o subdomínio é inválido"""
        return render(request, 'site/lojas/loja_404.html', status=400)





"""
class SubdominioMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split('.')

        # Tratar o acesso ao admin no domínio principal
        if host[0] == 'app' and host[1] == 'booksite' and host[2] == 'com':
            if request.path.startswith('/admin/'):
                return self.get_response(request)
            return self.render_subdominio_invalido(request)

        # Verifica se há um subdomínio
        if len(host) > 2:
            subdominio = host[0]  # Captura o subdomínio
            logger.debug(f"Subdomínio recebido: {subdominio}")
            try:
                request.loja = Loja.objects.get(subdominio=subdominio)  # Busca a loja pelo subdomínio
            except Loja.DoesNotExist:
                logger.warning(f"Nenhuma loja encontrada para o subdomínio: {subdominio}")
                return self.render_subdominio_invalido(request)
        else:
            request.loja = None  # Não há subdomínio

        return self.get_response(request)

    def render_subdominio_invalido(self, request):
        return render(request, 'site/lojas/loja_404.html', status=400)
"""