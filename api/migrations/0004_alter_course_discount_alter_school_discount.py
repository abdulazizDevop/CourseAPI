# Generated by Django 5.1.6 on 2025-02-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_course_discount_alter_course_discount_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='discount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='school',
            name='discount',
            field=models.IntegerField(),
        ),
    ]
