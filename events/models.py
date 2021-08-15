import uuid
from datetime import date

from django.db import models
from django_countries.fields import CountryField

from employees.models import DirectiveEmployee, RegularEmployee
# Dependency Injection
SOLO_GROUP = (
    ('soloist', 'Soloist'),
    ('group', 'Group'),
)
# Create your models here.
class Event(models.Model):
    """
    Event model. Each event will feature multiple parades.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    slug = models.SlugField(db_index=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    directive = models.ForeignKey(
        DirectiveEmployee,
        on_delete=models.CASCADE,
        related_name='event_directive'
    )
    employees = models.ManyToManyField(RegularEmployee, related_name='event_employees')

    class Meta:
        ordering = ['-created']

class Designer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passport = models.CharField(max_length=20)
    country = CountryField()

    class Meta:
        ordering = ['last_name']

class Parade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='parade_event')
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE, related_name='parade_designer')
    date = models.DateField()
    time = models.TimeField()
    collection = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ended = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

class Genre(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artist_name = models.CharField(max_length=256)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='artist_genre')
    contract = models.BooleanField(default=False)
    salary = models.PositiveIntegerField()

    class Meta:
        ordering = ['artist_name']

class Group(models.Model):
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Soloist(models.Model):
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, models.DO_NOTHING, blank=True, null=True)
