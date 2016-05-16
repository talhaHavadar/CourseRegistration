import requests
import json

STUDENTS_API_URL = "http://192.168.1.5:8000/api/students/" # "./json/student.json" # change to local ip of student page
STUDENTS_VALIDATE_API_URL = "http://192.168.1.5:8000/api/students/validation"
COURSE_API_URL = ""
TRANSCRIPT_API_URL = ""
INSTRUCTOR_API_URL = ""

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

def getCourses(semester):
    return [
      {
        "id" : 125,
        "semester": 6,
        "code" : "CME3008",
        "name": "Circuit Falan filan" ,
        "instructor_id" : 21,
        "start_time": "13:00:00",
        "end_time": "14:15:00",
        "quata": 25
      },
      {
        "id" : 128,
        "semester": 6,
        "code" : "CME3006",
        "name": "Network falan" ,
        "instructor_id" : 25,
        "start_time": "10:00:00",
        "end_time": "12:15:00",
        "quata": 40
      }]

def getTranscript(studentNo):
    return { "cumulative": 4.0 }

def getInstructor(id):
    return {
        "ID":19,
        "Name":"Burcu Yankovan",
        "PersonalID":551212,
        "Course":"CME3004",
        "Email":"burcu@hotmail.com",
        "PhoneNumber":"5451236"
      };

def getInstructors():
    pass
