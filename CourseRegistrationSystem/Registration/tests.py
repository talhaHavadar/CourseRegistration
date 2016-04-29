from django.test import TestCase
from Registration.models import CourseInfo
from Registration.models import Schedule
from Registration.models import Settings
# Create your tests here.

class CourseInfoTestCase(TestCase):
	def setUp(self):
		semester = Semester(name="2015-2016 Güz")
		semester.save()
		CourseInfo.objects.create(start_time = "12:00", end_time = "14:00", code= "CME3008", instructor_name = "Prf.Dr.Hafize Şen Çakır", days = 1)
		info = CourseInfo.objects.all()[0]
		Schedule.objects.create(student_id = 3, comfirmed = False, courses = info, semester = semester)
		Settings.objects.create(on_registration = True)

	def test_can_schedule_added(self):
		info = CourseInfo.objects.get(code = "CME3008")
		schedule = Schedule.objects.get(id = 1)
		semester = Semester.objects.get(id = 1)
		settings = Settings.objects.get(id = 1)
		self.assertEqual(Semester.id, 1)
		self.assertEqual(CourseInfo.id, 1)
		self.assertEqual(CourseInfo.days, 1)
		self.assertEqual(CourseInfo.instructor_name, "Prf.Dr.Hafize Şen Çakır")
		self.assertEqual(len(Semester.objects.filter(id__gte = 1)),1)
		self.assertEqual(len(CourseInfo.objects.all()),1)	
		self.assertEqual(len(Schedule.objects.all()),1)
		self.assertEqual(len(Settings.objects.all()),1)
		self.assertEqual(schedule.student_id,3)
		self.assertEqual(schedule.comfirmed, False)
		self.assertEqual(info.start_time,"12:00")
		self.assertEqual(info.end_time,"14:00")
		self.assertEqual(info.code,"CME3008")
		self.assertEqual(settings.on_registration, True)
		self.assertEqual(len(Semester.objects.all()), 1)
		self.assertEqual(semester.objects.name, "2015-2016 Güz")
