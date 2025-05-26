from rest_framework import serializers
from .models import Employee, AttendanceRecord

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'document', 'first_name', 'last_name']


class AttendanceRecordSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_document = serializers.CharField(write_only=True)

    class Meta:
        model = AttendanceRecord
        fields = ['id', 'employee', 'employee_document', 'date', 'time']

    def create(self, validated_data):
        document = validated_data.pop('employee_document')
        try:
            employee = Employee.objects.get(document=document)
        except Employee.DoesNotExist:
            raise serializers.ValidationError({'employee_document': 'Employee with this document does not exist.'})
        attendance_record = AttendanceRecord.objects.create(employee=employee, **validated_data)
        return attendance_record
