from django.shortcuts import render, redirect
from django.views import View
from .models import Department, Faculty, Session, Semester, Course, Student, RegisteredCourse, StudentGrade
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class RegisterCourse(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        session = Session.objects.all().order_by("-timestamp")

        context = {
            "session": session,
        }
        return render(request, "portal/register-course.html", context)

    def post(self, request, *args, **kwargs):
        logged_in_user = request.user
        user_session = request.POST.get("session")
        user_semester = request.POST.get("semester")
        student = Student.objects.get(user=logged_in_user)
        semester = Semester.objects.all().order_by("-timestamp").first()
        session = Session.objects.all().order_by("-timestamp").first()
        old_session = Session.objects.all().order_by("-timestamp")[1]
        old_semester = Semester.objects.get(session=old_session, semester=user_semester)
        student_department = student.department
        student_level = student.level
        current_semester = semester.semester
        current_session = session.session
        already_registered = []
        not_registered = []
        old_courses = []
        courses = True
        if (user_session == current_session) and (user_semester == current_semester):
            semester_course = Course.objects.filter(department=student_department, semeter=user_semester, level=student_level)
            registered_course = RegisteredCourse.objects.filter(session=session, semester=semester)
            registered_course_previous_session = RegisteredCourse.objects.filter(session=old_session, semester=old_semester, student=student)
            student_grade_previous_session = StudentGrade.objects.filter(session=old_session, semester=old_semester, student=student)
            
            for course in semester_course:
                for reg_course in registered_course:
                    if (course.name == reg_course.course.name) and (request.user.student in reg_course.student.all()):
                        already_registered.append(course)

            for course in semester_course:
                if course not in already_registered:
                    not_registered.append(course)

            for old_course in registered_course_previous_session:
                for old_grade in student_grade_previous_session:
                    
                    if (old_course.course.code == old_grade.course.code) and (old_grade.grade == "F"):
                        print(old_grade.course.code, old_course.course.code)
                        old_courses.append(old_course.course)
                        
        else:
            courses = "closed"

        print(already_registered)
        print(not_registered)
        print(old_courses)
        context = {
            "already_registered":already_registered,
            "not_registered":not_registered,
            "courses":courses,
            "session": user_session,
            "semester": user_semester,
            "old_courses":old_courses
        }
        return render(request, "portal/register-course.html", context)


class UpdateCourse(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        logged_in_user = request.user
        student = Student.objects.get(user=logged_in_user)
        session = Session.objects.all().order_by("-timestamp").first()
        semester = Semester.objects.all().order_by("-timestamp").first()
        student_department = student.department
        current_semester = semester.semester
        for key in request.POST:
            if key != "csrfmiddlewaretoken":
                course_code = request.POST[key]
                course = Course.objects.get(code=course_code)
                if RegisteredCourse.objects.filter(session=session, semester=semester, course=course).exists():
                    already_existed = RegisteredCourse.objects.get(session=session, semester=semester, course=course)
                    print("here1")
                    already_existed.student.add(student)
                else:
                    new = RegisteredCourse(session=session, semester=semester, course=course)
                    new.save()
                    print("here2")
                    new.student.add(student)
        #student_dept_course = Course.objects.get(department=student_department)
        all_registered_courses = RegisteredCourse.objects.filter(session=session, semester=semester, student=student)
        for item in all_registered_courses:
            course_name = item.course.name
            x = request.POST.get(course_name)
            if x == None:
                is_student = False
                for j in item.student.all():
                    if j.user == request.user:
                        is_student = True
                        break
                if is_student:
                    print("here4")
                    item.student.remove(student)

        return redirect("portal:register_course")

class CheckResult(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logged_in_user = User.objects.get(id=request.user.id)
        student = Student.objects.get(user=logged_in_user)
        student_department = student.department
        session = Session.objects.all().order_by("-timestamp")
        semester = Semester.objects.all().order_by("-timestamp")
        course = Course.objects.filter(department=student_department).order_by("name")

        context = {
            "session":session,
            "semester":semester,
            "course":course
        }
        return render(request, "portal/result.html", context)

    def post(self, request, *args, **kwargs):
        logged_in_user = User.objects.get(id=request.user.id)
        student = Student.objects.get(user=logged_in_user)
        session = request.POST.get("session")
        semester = request.POST.get("semester")
        course_code = request.POST.get("course") 
        x_session =  Session.objects.get(session=session)
        #try
        x_semester = Semester.objects.get(semester=semester, session=x_session)
        if course_code != "all":
            x_course = Course.objects.get(code=course_code)
            try:
                result = StudentGrade.objects.get(session=x_session, semester=x_semester, student=student, course=x_course)
            except:
                result = "no_result"
        else:
            try:
                result = StudentGrade.objects.filter(session=x_session, semester=x_semester, student=student)
            except:
                result = "no_result"
      
        print(result)
        context = {
            "result":result,
            "session":session,
            "semester":semester,
            "course_code":course_code

        }
        return render(request, "portal/result.html", context)


class Grading(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        session = Session.objects.all().order_by("-timestamp")
        semester = Semester.objects.all().order_by("-timestamp")
        course = Course.objects.all().order_by("name")
        
        context = {
            "session":session,
            "semester":semester,
            "course":course
        }
        return render(request, "portal/grading.html", context)

    def post(self, request, *args, **kwargs):
        session = request.POST.get("session")
        semester = request.POST.get("semester")
        course_code = request.POST.get("course")
        print(session)
        print(semester)
        print(course_code)
        x_session =  Session.objects.get(session=session)
        #try
        x_semester = Semester.objects.get(semester=semester, session=x_session)
        x_course = Course.objects.get(code=course_code)
        registered_course = RegisteredCourse.objects.get(session=x_session, semester=x_semester, course=x_course)

        context = {
            "session":session,
            "semester":semester,
            "course_code":course_code,
            "registered_course":registered_course
        }
        return render(request, "portal/grading.html", context) 


class AddGrade(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        session = request.POST.get("session")
        semester = request.POST.get("semester")
        course_code = request.POST.get("course_code")
        x_session =  Session.objects.get(session=session)
        x_semester = Semester.objects.get(semester=semester, session=x_session)
        x_course = Course.objects.get(code=course_code)
        
        registered_course = RegisteredCourse.objects.get(session=x_session, semester=x_semester, course=x_course)

        for student in registered_course.student.all():
            x_student = Student.objects.get(reg_number=student)
            for item in request.POST:
                if item == f"{student}_ca":
                    student_ca = request.POST.get(f"{student}_ca")
                    student_exams = request.POST.get(f"{student}_exams")
                    student_total = request.POST.get(f"{student}_total")
                    student_grade = request.POST.get(f"{student}_grade")
                    
                    if StudentGrade.objects.filter(session=x_session, semester=x_semester, course=x_course, student=x_student).exists():
                        already_existed = StudentGrade.objects.get(session=x_session, semester=x_semester, course=x_course, student=x_student)
                        already_existed.ca = student_ca
                        already_existed.exams = student_exams
                        already_existed.total = student_total
                        already_existed.grade = student_grade
                        already_existed.save()
                        print("here1")
                        # already_existed.student.add(student)
                    else:
                        new = StudentGrade(session=x_session, semester=x_semester, course=x_course, student=x_student)
                        new.ca = student_ca
                        new.exams = student_exams
                        new.total = student_total
                        new.grade = student_grade
                        new.save()
                        print("here2")
                        # new.student.add(student)
        return redirect("portal:student_dashboard")


class StudentDashboard(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "portal/student-dashboard.html")


class LecturerDashboard(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "portal/lecturer-dashboard.html")