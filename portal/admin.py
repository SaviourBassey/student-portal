from django.contrib import admin
from .models import Session, Semester, Faculty, Department, Course, Student, RegisteredCourse, StudentGrade

# Register your models here.

admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(RegisteredCourse)
admin.site.register(StudentGrade)