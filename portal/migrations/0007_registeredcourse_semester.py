# Generated by Django 4.0.6 on 2022-07-10 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_alter_registeredcourse_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredcourse',
            name='semester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portal.semester'),
        ),
    ]
