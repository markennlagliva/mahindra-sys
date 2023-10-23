import django_filters

from .models import ExtendUser
from logs.models import Attendance

class ExtendUserFilter(django_filters.FilterSet):
    class Meta:
        model = ExtendUser
        fields = '__all__'

class AttendanceFilter(django_filters.FilterSet):
    class Meta:
        model = Attendance
        fields = '__all__'