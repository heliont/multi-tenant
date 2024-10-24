from django.contrib import admin
from django.urls import path, include

# Para arquivos estáticos
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

# Envolver a view admin com o decorator login_required
#admin.site.login = login_required(admin.site.login)

urlpatterns = [
    path('admin/', admin.site.urls),  # URL padrão para admin
    path('', include('tenant.urls')),  # View padrão para subdomínios
    path('', include('usuario.urls')),  # View login

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
