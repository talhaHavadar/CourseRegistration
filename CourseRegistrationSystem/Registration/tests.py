from django.test import TestCase
from Registration.models import CourseInfo
from Registration.models import Schedule
from Registration.models import Settings
from Registration.models import Semester
# Create your tests here.

class CourseInfoTestCase(TestCase):
	def setUp(self):
		semester = Semester(name="2015-2016 Güz")
		semester.save()
		CourseInfo.objects.create(start_time = "12:00", end_time = "14:00", code= "CME3008", instructor_name = "Prf.Dr.Hafize Şen Çakır", day = 1)
		info = CourseInfo.objects.all()[0]
		Schedule.objects.create(student_id = 3, confirmed = False, semester = semester)
		Settings.objects.create(on_registration = True)

	def test_can_schedule_added(self):
		info = CourseInfo.objects.get(code = "CME3008")
		schedule = Schedule.objects.get(id = 1)
		semester = Semester.objects.get(id = 1)
		settings = Settings.objects.get(id = 1)
		self.assertEqual(semester.id, 1)
		self.assertEqual(info.id, 1)
		self.assertEqual(info.day, 1)
		self.assertEqual(info.instructor_name, "Prf.Dr.Hafize Şen Çakır")
		self.assertEqual(len(Semester.objects.filter(id__gte = 1)),1)
		self.assertEqual(len(CourseInfo.objects.all()),1)
		self.assertEqual(len(Schedule.objects.all()),1)
		self.assertEqual(len(Settings.objects.all()),1)
		self.assertEqual(schedule.student_id,3)
		self.assertEqual(schedule.confirmed, False)
		self.assertEqual(str(info.start_time),"12:00:00")
		self.assertEqual(str(info.end_time),"14:00:00")
		self.assertEqual(info.code,"CME3008")
		self.assertEqual(settings.on_registration, True)
		self.assertEqual(len(Semester.objects.all()), 1)
		self.assertEqual(semester.name, "2015-2016 Güz")
