from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Schedule
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
    student = getStudent(request.session["user"]) or dict()

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
    semester = int(sClass) * 2
    now = arrow.now()
    if now.month > 9 and now.month < 2 :
        semester -= 1
    print("sClass", sClass, semester)
    return semester

def schedule(request):
    student = getStudent(request.session["user"])
    semester = calc_semester(student["class_no"])
    schedules = Schedule.objects.filter(semester__count = semester, student_id = student["studentNo"])
    print(schedules)
    if len(schedules) == 0:
        schedules = dict()
        courses = dict()
        message = "You haven't got any schedule."
    else:
        if schedules[0].confirmed:
            message = "Your schedule was confirmed."
        else:
            message = "Your schedule waiting for acceptance."
        schedules = schedules[0]
        courses = groupCourses(schedules.as_json()["courses"])
    monday = list()
    tuesday = list()
    wednesday = list()
    thursday = list()
    friday = list()
    saturday = list()

    days = {
        0: monday,
        1: tuesday,
        2: wednesday,
        3: thursday,
        4: friday,
        5: saturday
    }


    for key, val in courses.iteritems():
        days[key] = val
    return render(request, "Registration/schedule.html", { "student": student, "monday": days[0],
     "tuesday": days[1], "wednesday": days[2], "thursday": days[3], "friday": days[4], "saturday": days[5],
     "status_message": message })

def registration(request):

    student = getStudent(request.session["user"])
    semester = calc_semester(student["class_no"])
    schedules = Schedule.objects.filter(semester__count = semester, student_id = student["studentNo"])
    if len(schedules) > 0:
        return redirect("Registration:schedule")

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
        elif POST["method"] == "courses_up":
            student = getStudent(request.session["user"])
            sClass = student["class_no"]
            semester = calc_semester(int(sClass) +1)
            courses = getCourses(semester)
            return JsonResponse({"success":True, "courses": courses})
        elif POST["method"] == "registration" and POST.get("courses", False):
            courses = POST["courses"]
            schedule = setSchedule(request, courses)
            return JsonResponse({ "success": True, "schedule": schedule.as_json() })
        else:
            return JsonResponse({"success": False, "message": "Invalid method." })
    student = getStudent(request.session["user"])
    return render(request, "Registration/registration.html", { "student": student })

def logout(request):
    del request.session["user"]
    return redirect("Registration:login")

def index(request):
    # del request.session["user"]
    student = getStudent(request.session["user"]) or dict()
    return render(request, "Registration/mainPage.html", { "student": student })
