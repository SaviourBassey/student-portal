# Generated by Django 4.0.6 on 2022-07-10 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_registeredcourse_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredcourse',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.semester'),
        ),
    ]
