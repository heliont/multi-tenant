# admin.py no app de usuários (por exemplo, 'usuarios')

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Campos a serem exibidos no admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'tenant')
    fieldsets = UserAdmin.fieldsets + (  # Inclui os campos do UserAdmin padrão
        (None, {'fields': ('tenant',)}),  # Adiciona o campo tenant
    )

# Registra o CustomUser no admin
admin.site.register(CustomUser, CustomUserAdmin)