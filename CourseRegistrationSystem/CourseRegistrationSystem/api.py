from Registration.models import CourseInfo, Schedule, Semester, Settings
from rest_framework import routers, serializers, viewsets, filters, generics

class CourseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInfo
        fields = ("day", "code", "start_time", "end_time", "instructor_name", "id")

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('name',)

class ScheduleSerializer(serializers.ModelSerializer):
    semester = SemesterSerializer(read_only = True)
    courses = CourseInfoSerializer(many = True, read_only = True)
    class Meta:
        model = Schedule
        fields = ('id', 'student_id', 'confirmed', 'semester','courses')

class ScheduleFilter(filters.FilterSet):
    class Meta:
        model = Schedule
        fields = ("id", "confirmed", "student_id","courses__code")

class ScheduleList(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ScheduleFilter

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
