# Generated by Django 4.0.6 on 2022-07-12 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_alter_registeredcourse_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca', models.IntegerField()),
                ('exams', models.IntegerField()),
                ('total', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=1)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.semester')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.student')),
            ],
        ),
    ]
