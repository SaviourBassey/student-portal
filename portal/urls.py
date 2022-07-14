from django.urls import path
from . import views

app_name = "portal"

urlpatterns =[
    path("register-course/", views.RegisterCourse.as_view(), name="register_course"),
    path("update-course/", views.UpdateCourse.as_view(), name="update_course"),
    path("check-result/", views.CheckResult.as_view(), name="check_result"),
    path("student-grading/", views.Grading.as_view(), name="grading"),
    path("add-grade/", views.AddGrade.as_view(), name="add_grade"),
    path("student-dashboard/", views.StudentDashboard.as_view(), name="student_dashboard"),
    path("lecturer-dashboard/", views.LecturerDashboard.as_view(), name="lecturer_dashboard"),
]