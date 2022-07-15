from django.contrib import admin
from .models import (
    Session, Semester, Faculty, Department, Course, Student, RegisteredCourse, StudentGrade,
    CourseAdviser
)

# Register your models here.]

#Creating a custom admin page, probably another user, and the create its url in the base url
class PortalAdminArea(admin.AdminSite):
    index_title = "EUCRS ePortal"
    site_header = "Portal Admin Area"
    index_title = "EUCRS ePortal"

portal_site = PortalAdminArea(name="PortalAdmin")

#Register a model to the custom admin page
portal_site.register(Session)
portal_site.register(Semester)
portal_site.register(Faculty)
portal_site.register(Department)
portal_site.register(Course)
portal_site.register(Student)
portal_site.register(RegisteredCourse)
portal_site.register(StudentGrade)
portal_site.register(CourseAdviser)


admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(RegisteredCourse)
admin.site.register(StudentGrade)
admin.site.register(CourseAdviser)