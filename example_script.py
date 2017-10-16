import django
from django.conf import settings

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'swapi.settings'
django.setup()

# Now this script or any imported module can use any part of Django it needs.
from api import models


if __name__ == '__main__':
    # Put your code here
    print("Total Transport objects:", models.Transport.objects.count())