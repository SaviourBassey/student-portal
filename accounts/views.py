from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from portal.models import Student

# Create your views here.

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/login.html")

    def post(self, request, *args, **kwargs):
        reg_number = str(request.POST.get('reg_number')).upper()
        password = request.POST.get('password')
        try:
            student = Student.objects.get(reg_number=reg_number)
        except:
            student = None
        if student is not None:
            student_username = student.user.username
            user = authenticate(request, username=student_username, password=password)
            if user is not None:
                login(request, user)
                return redirect("portal:student_dashboard")
            else:
                return redirect("accounts:login")
        else:
                return redirect("accounts:login")


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("accounts:login")