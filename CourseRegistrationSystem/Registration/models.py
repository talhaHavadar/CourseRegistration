from django.db import models
from model_utils import Choices
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class CourseInfo(models.Model):
	DAYS = Choices(
		(0, 'Monday', _('Monday')),
		(1, 'Tuesday', _('Tuesday')),
		(2, 'Wednesday', _('Wednesday')),
		(3, 'Thursday', _('Thursday')),
		(4, 'Friday', _('Friday')),
		(5, 'Saturday', _('Saturday')))

	start_time = models.TimeField()
	end_time = models.TimeField()
	code = models.CharField(max_length = 7)
	instructor_name = models.CharField(max_length = 100)
	day = models.IntegerField(choices = DAYS, default = DAYS.Monday)

	def __str__(self):
		return u"{} - {}".format(self.code, self.instructor_name)

	def as_json(self):
		return dict(
			start_time= self.start_time,
			end_time = self.end_time,
			code = self.code,
			instructor_name = self.instructor_name,
			day = self.day
		)

class Schedule(models.Model):
	student_id = models.CharField(max_length=20)
	confirmed = models.BooleanField(default = False)
	semester = models.ForeignKey(
		'Semester',
		on_delete = models.CASCADE)
	courses = models.ManyToManyField(CourseInfo, related_name = 'schedule')

	class Meta:
		unique_together = (("student_id","semester"),)

	def __str__(self):
		return u"{} | {}".format(self.student_id, self.semester.name)

	def as_json(self):
		courseList = list()
		for course in self.courses.all():
			courseList.append(course.as_json())
		return dict(
			student_id= self.student_id,
			confirmed= self.confirmed,
			semester= self.semester.as_json(),
			courses= courseList
		)
class Semester(models.Model):
	count = models.IntegerField()
	name = models.CharField(max_length=25, unique=True)
	def __str__(self):
		return u"{} | {}".format(self.count,self.name)

	def as_json(self):
		return dict(
			count= self.count,
			name= self.name
		)

class Settings(models.Model):
	on_registration = models.BooleanField(default = False)
