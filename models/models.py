import uuid
from django_countries.fields import CountryField

from django.db import models

# Dependency injection
EYE_COLORS = (
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('brown', 'Brown'),
    ('hazel', 'Hazel'),
    ('gray', 'Gray'),
    ('dark', 'Dark'),
    ('other', 'Other'),
)
SKIN_COLORS = (
    ('black', 'Black'),
    ('brown', 'Brown'),
    ('olive', 'Olive'),
    ('fair', 'Fair'),
    ('pale', 'Pale'),
)
# Create your models here.
class ModelAgency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    country = CountryField()
    creation_year = models.DateField()
    email = models.EmailField()
    owner_name = models.CharField(max_length=512)
    parent_agency = models.ForeignKey('self', models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['name']

class Measurements(models.Model):
    chest = models.SmallIntegerField()
    waist = models.SmallIntegerField()
    hips = models.SmallIntegerField()

class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = CountryField()
    birthday = models.DateField()
    eye_color = models.CharField(choices=EYE_COLORS, max_length=10)
    skin_color = models.CharField(choices=SKIN_COLORS, max_length=20)
    height = models.SmallIntegerField()
    shoe_size = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    particularities = models.TextField()
    measurements = models.ForeignKey(Measurements, on_delete=models.DO_NOTHING, related_name='model_measurements')
    active = models.BooleanField(default=True)
    salary = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name']
