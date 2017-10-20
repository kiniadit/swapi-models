import django
from django.conf import settings
from django.db.models import Count

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'swapi.settings'
django.setup()

# Now this script or any imported module can use any part of Django it needs.
from api import models


if __name__ == '__main__':
    print("Total Starship objects:", models.Starship.objects.count())
    print("Total films made by George Lucas: ", models.Film.objects.filter(director='George Lucas').count())
    print("Latest film made by George Lucas: ", models.Film.objects.filter(director='George Lucas').order_by('-release_date')[0])
    print("Starship with id 15: ", models.Starship.objects.get(id=15))
    print("The above Starship was in ", models.Film.objects.filter(starships__name=models.Starship.objects.filter(id=15).first()).count(),"films")
    print("CR90 corvette Starship was in ", models.Film.objects.filter(starships__name__contains='CR90 ').count(),"films")
    print("The film with the fewest starships is ", models.Film.objects.annotate(num_starships=Count('starships')).order_by('num_starships')[0].title)
    print("The films that Luke Skywalker did not appear in are", " & ".join(a.title for a in models.Film.objects.exclude(characters__name__contains='Luke Skywalker')))
    print("There are", models.Starship.objects.filter(name__icontains='fight').count(),"starships with the word 'fight' in it")
    print("The cheapest starship is", models.Starship.objects.order_by('cost_in_credits').first())