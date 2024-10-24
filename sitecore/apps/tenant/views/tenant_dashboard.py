from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from tenant.models import Loja

class TenantDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'tenant/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_superuser:
            # Se o usuário for um superusuário, exiba todas as lojas
            context['lojas'] = Loja.objects.all()
        elif hasattr(self.request.user, 'tenant'):
            # Se o usuário for comum, exiba apenas a loja do seu tenant
            context['loja'] = self.request.user.tenant.lojas_tenant  # Acesse a única loja do tenant usando o related_name
        else:
            context['loja'] = None  # Nenhuma loja se o usuário não tiver um tenant

        return context