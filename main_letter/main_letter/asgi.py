"""
ASGI config for main_letter project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from letter import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_letter.settings')

application = get_asgi_application()
