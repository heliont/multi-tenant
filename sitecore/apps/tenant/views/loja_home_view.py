# views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from ..models import Produto

class LojaHomeView(TemplateView):
    template_name = 'site/loja_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loja = self.request.loja  # A loja será injetada pelo middleware
        context['loja'] = loja
        if loja:
            context['produtos'] = Produto.objects.filter(loja=loja)
            
        else:
            context['produtos'] = []  # No caso de loja não encontrada, exibe uma lista vazia
        return context
