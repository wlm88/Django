"""
WSGI config for myDJ project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myDJ.settings')

application = get_wsgi_application()

#
# sys.path.append('D:\keshe\LOG\LOG')
# sys.path.append('D:\office\python\Lib\site-packages\django\bin')