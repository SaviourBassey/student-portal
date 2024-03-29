# Generated by Django 4.0.6 on 2022-07-12 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_studentgrade'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgrade',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='studentgrade',
            name='total',
            field=models.IntegerField(),
        ),
    ]
