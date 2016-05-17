# coding=utf-8

import requests
import json
import arrow
from underscore import _
from .models import *

STUDENTS_API_URL = "http://194.27.104.26:8000/api/students/" # "./json/student.json" # change to local ip of student page
STUDENTS_VALIDATE_API_URL = "http://194.27.104.26:8000/api/students/validation"
COURSE_API_URL = "http://161.9.133.127/multitier/webservice/courses.php"
TRANSCRIPT_API_URL = "http://161.9.134.198:8080/transcriptSystem/webservice/TranscriptRequest.php"
INSTRUCTOR_API_URL = "http://194.27.104.175/webservice.php"

COURSE_DAYS = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
}

def getStudent(student_no):
    payload = {
        "format" : "json",
        "studentNo": student_no
    }
    r = requests.get(STUDENTS_API_URL, params = payload)
    data = r.json()
    if len(data) != 0:
        advisor = getInstructor(data[0]["advisorId"])
        transcript = getTranscript(data[0]["studentNo"])
        data[0]["advisor"] = advisor
        data[0]["transcript"] = transcript
        return data[0]
    else:
        return None

def isStudentValid(student_no, password):
    r = requests.post(STUDENTS_VALIDATE_API_URL, data= { "studentNo": student_no,"password": password })
    data = r.json()
    if data["success"]:
        return (True, data["message"])
    else:
        return (False, data["message"])
    return False

def getCourse(code):
    pass

def groupCourses(courses):
    sortedC = _.sortBy(courses, 'time')
    groupedCourses = _.groupBy(sortedC, "day")
    return groupedCourses

def getCourses(semester):
    courses = list()
    courses.append({"id" : 125,"semester": 6,"code" : "CME3008","name": "Circuit Falan filan" ,"instructor_id" : 16,"start_time": "13:00:00","end_time": "14:15:00","quata": 25})
    courses.append({"id" : 128,"semester": 6,"code" : "CME3006","name": "Network falan","instructor_id" : 30,"start_time": "10:00:00","end_time": "12:15:00","quata": 40 })
    courses.append({"id" : 130,"semester": 6,"code" : "CME3006","name": "Network falan","instructor_id" : 28,"start_time": "10:00:00","end_time": "12:15:00","quata": 40 })
    r = requests.post(COURSE_API_URL, data= { "format": "json" })
    courses = r.json()
    for c in courses:
        instructor = getInstructor(c["instructor"])
        c["instructor"] = instructor

    return courses

def getTranscript(studentNo):
    try:
        #r = requests.post(TRANSCRIPT_API_URL, data = {"studentNumber": studentNo})
        transcript = r.json()
        transcript = transcript["transcript"]
    except Exception as e:
        transcript = dict()
        transcript["Cumulative"] = 4.0
    return { "cumulative": transcript["Cumulative"] }

def getInstructor(id):
    r = requests.post(INSTRUCTOR_API_URL, data = { "id": id })
    instructors = r.json()
    if len(instructors) > 0:
        return instructors[0]
    return None

def setSchedule(request, courses):
    user = request.session["user"]
    if courses[0]["semester"] % 2 == 0:
        now = arrow.now()
        semString = "{}-{} {}".format(now.year - 1, now.year,"Spring Semester")
        semester,c = Semester.objects.get_or_create(count=courses[0]["semester"], name = semString)
    else:
        now = arrow.now()
        semString = "{}-{} {}".format(now.year, now.year + 1,"Fall Semester")
        semester,c = Semester.objects.get_or_create(count=courses[0].semester, name = semString)
    schedule = Schedule.objects.create(student_id = user, confirmed = False,semester = semester)
    for course in courses:
        day = COURSE_DAYS[course["days"]]
        c, created = CourseInfo.objects.get_or_create(code=course["courseCode"], start_time= course["start_time"],
        end_time= course["end_time"], instructor_name = course["instructor"]["Name"], day = day)
        schedule.courses.add(c)
    schedule.save()
    return schedule

def getInstructors():
    r = requests.get(INSTRUCTOR_API_URL)
    instructors = r.json()
    return instructors
