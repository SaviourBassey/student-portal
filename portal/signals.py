from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Session, Student


@receiver(post_save, sender=Session)
def update_level(sender, **kwargs):
    all_student = Student.objects.all()
    for student in all_student:
        level = Student.objects.get(id=student.id)
        level.level  = level.level + 100
        level.save()
        
        if (level.faculty.name == "ENGINERRING") and (level.level >= 500):
            level.level  = 500
            level.save()
        elif (level.faculty.name != "ENGINERRING") and (level.level >= 400):
            level.level  = 400
            level.save()


