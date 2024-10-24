#!/usr/bin/env python

"""
Django SECRET_KEY generator.
"""
from django.utils.crypto import get_random_string


chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

CONFIG_STRING = """
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS=127.0.0.1, .localhost
#DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
#DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME?init_command=SET sql_mode='STRICT_TRANS_TABLES'&charset=utf8mb4

#SECURE_SSL_REDIRECT=True
#CSRF_TRUSTED_ORIGINS=http://seusite.com, http://www.seusite.com, https://seusite.com, https://www.seusite.com
# Modo de alternar entre settings: Principal=main, Desenvolvedor=dev, Produção=prod
#CONFIGURATION_SITE=nomeprojeto.dev


# Redis Acesso/Porta
# - Somente um pode ficar ativado.
# Redis Local e Dev Host precisa estar com CONFIGURATION_SITE no modo Dev.

## Redis Local
#REDIS_LOCAL=False
#REDIS_LOCAL_PORT=redis://127.0.0.1:4444

## Redis Dev Host
#REDIS_DEV_HOST=False
#REDIS_DEV_HOST_PORT=redis://127.0.0.1:4444

## Redis Prod Host
#REDIS_PROD_HOST=False
#REDIS_PROD_HOST_PORT=redis://127.0.0.1:4444

# Para usar exclusivamente na hospedagem CPANEL
STATIC_STATUS=False
STATIC_ROOT='/home/user/pasta/static'
MEDIA_ROOT='/home/user/pasta/media'


# Configurações de envio do e-mail
#DEFAULT_FROM_EMAIL=
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = ''
#EMAIL_PORT = 
#EMAIL_USE_TLS = True
#EMAIL_HOST_USER = ""
#EMAIL_HOST_PASSWORD = ""

""".strip() % get_random_string(50, chars)

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)
