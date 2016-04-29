from django.db import models
from model_utils import Choices
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

class Schedule(models.Model):
	student_id = models.IntegerField()
	confirmed = models.BooleanField(default = False)
	semester = models.ForeignKey(
		'Semester',
		on_delete = models.CASCADE)
	courses = models.ManyToManyField(CourseInfo, related_name = 'schedule')

	class Meta:
		unique_together = (("student_id","semester"),)
class Semester(models.Model):
	name = models.CharField(max_length = 25, unique = True)

class Settings(models.Model):
	on_registration = models.BooleanField(default = False)
