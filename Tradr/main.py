from django.core.wsgi import get_wsgi_application

import os


# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tradr.settings")

# Start the WSGI application
application = get_wsgi_application()