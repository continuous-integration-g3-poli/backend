import django_filters
from .models import AttendanceRecord
    
class AttendanceRecordFilter(django_filters.FilterSet):
    employee_document = django_filters.CharFilter(field_name='employee__document')

    class Meta:
        model = AttendanceRecord
        fields = ['date', 'employee_document']