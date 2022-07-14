# Generated by Django 4.0.6 on 2022-07-10 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_alter_student_department_alter_student_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('course', models.ManyToManyField(to='portal.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.faculty')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.semester')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.student')),
            ],
        ),
    ]
