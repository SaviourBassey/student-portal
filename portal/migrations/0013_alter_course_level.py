# Generated by Django 4.0.6 on 2022-07-13 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_course_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.IntegerField(choices=[(100, 100), (200, 200), (300, 300), (400, 400), (500, 500)]),
        ),
    ]
