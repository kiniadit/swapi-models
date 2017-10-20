from django.db import models


# You will need the following:
# models.CharField
# models.ForeignKey
# https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types

class TimeStampedModel(models.Model):
    edited = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)    
   
    class Meta:
        abstract=True



class Planet(TimeStampedModel):
    climate = models.CharField(max_length=80)
    surface_water = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    diameter = models.CharField(max_length=80)
    rotation_period = models.CharField(max_length=80)
    terrain = models.CharField(max_length=80)
    gravity = models.CharField(max_length=80)
    orbital_period = models.CharField(max_length=80)
    population = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class People(TimeStampedModel):

    name = models.CharField(max_length=80)
    gender = models.CharField(max_length=80)
    skin_color = models.CharField(max_length=80)
    hair_color = models.CharField(max_length=80)
    height = models.CharField(max_length=80)
    eye_color = models.CharField(max_length=80)
    mass = models.CharField(max_length=80)
    homeworld = models.IntegerField()
    birth_year = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Species(TimeStampedModel):
    
    classification = models.CharField(max_length=80)
    people = models.ManyToManyField(
        People,
        related_name="species",
        blank=True
    )
    name = models.CharField(max_length=80)
    designation = models.CharField(max_length=80)
    eye_colors = models.CharField(max_length=80)
    skin_colors = models.CharField(max_length=80)
    language = models.CharField(max_length=80)
    hair_colors = models.CharField(max_length=80)
    homeworld = models.IntegerField(null=True)
    average_lifespan = models.CharField(max_length=80)
    average_height = models.CharField(max_length=80) 

    class Meta:
        verbose_name_plural = "species"

    def __str__(self):
        return self.name

class Transport(TimeStampedModel):

    name = models.CharField(max_length=40)
    model = models.CharField(max_length=80)
    crew = models.CharField(max_length=80)
    manufacturer = models.CharField(max_length=80)
    cost_in_credits = models.IntegerField()
    length = models.CharField(max_length=40)
    max_atmosphering_speed = models.CharField(max_length=40)
    passengers = models.CharField(max_length=40)
    cargo_capacity = models.CharField(max_length=40)
    consumables = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Starship(Transport):
    """ A starship is a transport with a hypderdrive """

    hyperdrive_rating = models.CharField(max_length=40)

    MGLT = models.CharField(max_length=40)

    starship_class = models.CharField(max_length=40)

    pilots = models.ManyToManyField(
        People,
        related_name="starships",
        blank=True
    )


class Vehicle(Transport):
    """ A vehicle is anything without hyperdrive capability """

    vehicle_class = models.CharField(max_length=40)

    pilots = models.ManyToManyField(
        'People',
        related_name="vehicles",
        blank=True
    )


class Film(TimeStampedModel):

    title = models.CharField(max_length=100)
    episode_id = models.IntegerField()
    opening_crawl = models.TextField(max_length=1000)
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    release_date = models.DateField()

    characters = models.ManyToManyField(
        People,
        related_name="films",
        blank=True
    )

    planets = models.ManyToManyField(
        Planet,
        related_name="films",
        blank=True
    )

    starships = models.ManyToManyField(
        Starship,
        related_name="films",
        blank=True
    )

    vehicles = models.ManyToManyField(
        Vehicle,
        related_name="films",
        blank=True
    )

    species = models.ManyToManyField(
        Species,
        related_name="films",
        blank=True
    )

    def __str__(self):
        return self.title
