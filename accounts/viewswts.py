from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Employee, AttendanceRecord
from .serializers import EmployeeSerializer, AttendanceRecordSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AttendanceRecordFilter


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__' 
        
class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AttendanceRecordFilter

    @action(detail=False, methods=['get'])
    def by_date(self, request):
        date = request.query_params.get('date')
        if not date:
            return Response({'error': 'Date parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        records = self.get_queryset().filter(date=date)
        serializer = self.get_serializer(records, many=True)
        return Response(serializer.data)
