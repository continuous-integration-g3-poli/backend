from .views import login_view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewswts import EmployeeViewSet, AttendanceRecordViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceRecordViewSet)


urlpatterns = [
    path('login/', login_view),
] + router.urls
