# Generated by Django 4.0.6 on 2022-07-10 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_remove_registeredcourse_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.course'),
        ),
    ]