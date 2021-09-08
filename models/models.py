import uuid
from django_countries.fields import CountryField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class ModelAgency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=200, unique=True)
    country = CountryField()
    creation_year = models.DateField()
    email = models.EmailField()
    owner_name = models.CharField(max_length=512)
    parent_agency = models.ForeignKey('self', models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'model agencies'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('models:agency_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ModelAgency, self).save(*args, **kwargs)

class Models(models.Model):
    # Dependency injection
    EYE_COLORS = (
        (None, 'Selecciona un color...'),
        ('green', 'Verdes'),
        ('blue', 'Azules'),
        ('brown', 'Cafés'),
        ('hazel', 'Miel'),
        ('gray', 'Grises'),
        ('dark', 'Negros'),
        ('other', 'Otro'),
    )
    SKIN_COLORS = (
        (None, 'Selecciona un color...'),
        ('black', 'Negra'),
        ('brown', 'Morena'),
        ('olive', 'Trigueña'),
        ('fair', 'Clara'),
        ('pale', 'Blanca'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    country = CountryField()
    birthday = models.DateField()
    eye_color = models.CharField(choices=EYE_COLORS, max_length=10)
    skin_color = models.CharField(choices=SKIN_COLORS, max_length=20)
    height = models.SmallIntegerField()
    shoe_size = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    particularities = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    salary = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    agency = models.ForeignKey(ModelAgency, related_name='model_modelagency', on_delete=models.CASCADE)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('models:model_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        name = self.first_name + ' ' + self.last_name
        self.slug = slugify(name)
        super(Models, self).save(*args, **kwargs)
        measures = Measurements.objects.filter(
            measured_model=self
        ).first()
        portfolio = Portfolio.objects.filter(
            model=self
        ).first()
        if not measures:
            Measurements.objects.create(
                measured_model=self
            )
        if not portfolio:
            Portfolio.objects.create(
                model=self
            )


class Measurements(models.Model):
    chest = models.SmallIntegerField(null=True)
    waist = models.SmallIntegerField(null=True)
    hips = models.SmallIntegerField(null=True)
    measured_model = models.ForeignKey(Models, on_delete=models.CASCADE, related_name='model_measures')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'model measurements'

class Portfolio(models.Model):
    model = models.ForeignKey(Models, on_delete=models.CASCADE, related_name='model_portfolio')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Portfolio for model {self.model}'

class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='photo_portfolio')
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
