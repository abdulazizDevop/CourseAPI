# Generated by Django 5.1.6 on 2025-02-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_course_discount_alter_school_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='discount_place',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='school',
            name='discount_place',
            field=models.IntegerField(),
        ),
    ]
