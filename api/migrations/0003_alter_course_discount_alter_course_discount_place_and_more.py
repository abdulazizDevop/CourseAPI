# Generated by Django 5.1.6 on 2025-02-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='discount',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='discount_place',
            field=models.IntegerField(max_length=6),
        ),
        migrations.AlterField(
            model_name='school',
            name='discount',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='school',
            name='discount_place',
            field=models.IntegerField(max_length=6),
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
