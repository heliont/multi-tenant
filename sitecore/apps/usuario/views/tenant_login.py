from django.contrib.auth import login
from django.views import View
from django.shortcuts import render, redirect

from sitecore.apps.usuario.forms import TenantLoginForm

class TenantLoginView(View):
    def get(self, request):
        form = TenantLoginForm()
        return render(request, 'tenant/login.html', {'form': form})

    def post(self, request):
        form = TenantLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('tenant:tenant_dashboard')  # Redireciona para o painel
        return render(request, 'tenant/login.html', {'form': form})
