from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
import arrow
from .api_handler import *

student = {
    "studentNo": "2013510047",
    "password": "22542256"
}

# Create your views here.
def login(request):
    if request.session.get("user", False):
        return redirect("Registration:index")
    if request.method == "POST":
        POST = json.loads(request.body.decode("utf-8"))
        no = POST["studentNo"]
        passwd = POST["password"]
        success, message = isStudentValid(no, passwd)
        if success:
            request.session["user"] = no;
            return JsonResponse({ "success": True, "studentNo": no })
        else:
            return JsonResponse({ "success": False, "message": message })
    return render(request, "Registration/login.html")

def pinfo(request):
    student = getStudent(request.session["user"])

    return render(request, "Registration/personalPage.html", { "student": student })

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def mail(request):
    subject = "Deneme"#request.POST.get('subject', '')
    message = "Deneme sdadasda123213"#request.POST.get('message', '')
    from_email = "havadartalha@gmail.com"#request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['gulgunpekmezci@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('successfull')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

def calc_semester(sClass):
    semester = sClass * 2
    now = arrow.now()
    if now.month > 9 and now.month < 2 :
        semester -= 1
    return semester

def registration(request):
    if request.method == "POST":
        POST = json.loads(request.body.decode("utf-8"))
        if POST["method"] == "courses":
            student = getStudent(request.session["user"])
            sClass = student["class_no"]
            semester = calc_semester(sClass)
            courses = getCourses(semester)
            return JsonResponse({"success": True, "courses": courses})
        elif POST["method"] == "me":
            student = getStudent(request.session["user"])
            student["semester"] = calc_semester(student["class_no"])
            return JsonResponse({ "success": True, "student": student })
        else:
            return JsonResponse({"success": False, "message": "Invalid method." })
    student = getStudent(request.session["user"])
    return render(request, "Registration/registration.html", { "student": student })

def logout(request):
    del request.session["user"]
    return redirect("Registration:login")

def index(request):
    # del request.session["user"]
    student = getStudent(request.session["user"])
    return render(request, "Registration/mainPage.html", { "student": student })
