from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Session(models.Model):
    session = models.CharField(max_length=9)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Session")
        verbose_name_plural = ("Session")

    def __str__(self):
        return self.session

SEMSTER_CHOICES = (
    ("1st", "1st"),
    ("2nd", "2nd")
)
class Semester(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10, choices=SEMSTER_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.semester} Semester of {self.session}"

class Faculty(models.Model):
    name = models.CharField(max_length=1000)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



SEMSTER_COURSE_CHOICES = (
    ("1st", "1st"),
    ("2nd", "2nd")
)
SEMSTER_LEVEL_CHOICES = (
    (100, 100),
    (200, 200),
    (300, 300),
    (400, 400),
    (500, 500)
)
class Course(models.Model):
    faculty = models.ManyToManyField(Faculty)
    department = models.ManyToManyField(Department)
    semeter = models.CharField(max_length=10, choices=SEMSTER_COURSE_CHOICES)
    level = models.IntegerField(choices=SEMSTER_LEVEL_CHOICES)
    name = models.CharField(max_length=1000)
    code = models.CharField(max_length=6)
    credit_load = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=16, unique=True)
    level = models.IntegerField(default=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reg_number

DEPARTMENT_LEVEL_CHOICES = (
    (100, 100),
    (200, 200),
    (300, 300),
    (400, 400),
    (500, 500)
)
class CourseAdviser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=11, unique=True)
    level = models.IntegerField(choices=DEPARTMENT_LEVEL_CHOICES)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id


class RegisteredCourse(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    # faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.name

GRADE_CHOICES = (
    ("A","A"),
    ("B","B"),
    ("C","C"),
    ("D","D"),
    ("E","E"),
    ("F","F")
)
class StudentGrade(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    # faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ca = models.IntegerField()
    exams = models.IntegerField()
    total = models.IntegerField()
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.reg_number} grade on {self.course.name}"

