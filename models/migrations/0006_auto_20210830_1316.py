# Generated by Django 3.2.6 on 2021-08-30 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_auto_20210830_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='model',
            name='eye_color',
            field=models.CharField(choices=[(None, 'Selecciona un color...'), ('green', 'Verdes'), ('blue', 'Azules'), ('brown', 'Cafés'), ('hazel', 'Miel'), ('gray', 'Grises'), ('dark', 'Negros'), ('other', 'Otro')], max_length=10),
        ),
        migrations.AlterField(
            model_name='model',
            name='particularities',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='model',
            name='skin_color',
            field=models.CharField(choices=[(None, 'Selecciona un color...'), ('black', 'Negra'), ('brown', 'Morena'), ('olive', 'Trigueña'), ('fair', 'Clara'), ('pale', 'Blanca')], max_length=20),
        ),
    ]
