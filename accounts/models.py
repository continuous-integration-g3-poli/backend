from django.db import models

class Employee(models.Model):
    document = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.document})"


class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        unique_together = ('employee', 'date', 'time')

    def __str__(self):
        return f"Attendance {self.employee.document} on {self.date} at {self.time}"
