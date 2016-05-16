from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json

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
        print("post", POST)
        if no and student['studentNo'] == no:
            if POST["password"] and POST["password"] == student['password']:
                request.session["user"] = no;
                return JsonResponse({ "success": True, "studentNo": no })
            else:
                return JsonResponse({ "success": False, "message": "Password is wrong!!" })
        return JsonResponse({ "success": False, "message": "Wrong student number!!" })
    return render(request, "Registration/login.html")

def pinfo(request):
    return render(request, "Registration/personalPage.html")

def logout(request):
    return HttpResponse("Deneme bir ki")

def index(request):
    # del request.session["user"]
    return render(request, "Registration/mainPage.html")
