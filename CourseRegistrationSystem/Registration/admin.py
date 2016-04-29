from django.contrib import admin
from Registration.models import CourseInfo, Schedule, Semester, Settings
# Register your models here.
@admin.register(CourseInfo)
class CourseInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    pass


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass
