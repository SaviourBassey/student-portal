# Generated by Django 4.0.6 on 2022-07-10 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_remove_registeredcourse_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeredcourse',
            name='course',
        ),
        migrations.AddField(
            model_name='registeredcourse',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portal.course'),
        ),
        migrations.RemoveField(
            model_name='registeredcourse',
            name='student',
        ),
        migrations.AddField(
            model_name='registeredcourse',
            name='student',
            field=models.ManyToManyField(to='portal.student'),
        ),
    ]
