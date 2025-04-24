import os
from django.core.wsgi import get_wsgi_application

# Defina a configuração do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_sj.settings')

# Crie a aplicação WSGI
application = get_wsgi_application()
