# Generated by Django 3.2.6 on 2021-08-20 02:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('artist_name', models.CharField(max_length=256)),
                ('contract', models.BooleanField(default=False)),
                ('salary', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['artist_name'],
            },
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('passport', models.CharField(max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('slug', models.SlugField()),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('directive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_directive', to='employees.directiveemployee')),
                ('employees', models.ManyToManyField(related_name='event_employees', to='employees.RegularEmployee')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('artist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Soloist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.artist')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='events.group')),
            ],
        ),
        migrations.CreateModel(
            name='Parade',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('collection', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('ended', models.BooleanField(default=False)),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parade_designer', to='events.designer')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parade_event', to='events.event')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_genre', to='events.genre'),
        ),
    ]
