from django.urls import path
# Para importar função
#from . import views
# Para importar CBV (Class Based View)
from .views import *

app_name = 'tenant'

urlpatterns = [
    path('', LojaHomeView.as_view(), name='list-veiculo'),
    path('painel/', TenantDashboardView.as_view(), name='tenant_dashboard'),

]
