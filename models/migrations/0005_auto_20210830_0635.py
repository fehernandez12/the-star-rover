# Generated by Django 3.2.6 on 2021-08-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_model_agency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurements',
            name='chest',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='hips',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='waist',
            field=models.SmallIntegerField(null=True),
        ),
    ]
