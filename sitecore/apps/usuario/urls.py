from django.urls import path
# Para importar função
#from . import views
# Para importar CBV (Class Based View)
from .views import *

app_name = 'usuario'

urlpatterns = [
    path('login/', TenantLoginView.as_view(), name='tenant_login'),

]
