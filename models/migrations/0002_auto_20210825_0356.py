# Generated by Django 3.2.6 on 2021-08-25 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurements',
            options={'ordering': ['-created'], 'verbose_name_plural': 'model measurements'},
        ),
        migrations.AlterModelOptions(
            name='modelagency',
            options={'ordering': ['name'], 'verbose_name_plural': 'model agencies'},
        ),
    ]
