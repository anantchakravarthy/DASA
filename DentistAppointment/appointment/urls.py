"""
doctor_appointment_system URL Configuration

"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import include, path, reverse_lazy

from .views import *

app_name = 'appointment'

urlpatterns = [
    path('service', ServiceView.as_view(), name='service'),
    path('patient-take-appointment/', TakeAppointmentView.as_view(), name='take-appointment'),
    path('dentist-create-appointment/', CreateAppointmentView.as_view(), name='create-appointment'),
    path('my-appointments/', AppointmentListView.as_view(), name='my-appointments'),
    path('<pk>/delete/', AppointmentDeleteView.as_view(), name='delete-appointment'),
    path('<pk>/create-log/', CreateLogView.as_view(), name="create-log"),
    path('<pk>/view-logs/', LogListView.as_view(), name='view-logs'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # path('', HomePageView.as_view(), name='home'),
    # path('service', ServiceView.as_view(), name='service'),
    # path('patient-take-appointment/', TakeAppointmentView.as_view(), name='take-appointment'),
    # path('my-appointments/', AppointmentListView.as_view(), name='my-appointments'),
    # path('<pk>/delete/', AppointmentDeleteView.as_view(), name='delete-appointment'),
    # path('dental_log/<pk>', DentistLogView.as_view(), name='dental-log'),
    # path('search/', SearchView.as_view(), name='search'),
    # path('patient/', PatientListView.as_view(), name='patient-list'),
    #path('patients/<int:appointment_id>', PatientPerAppointmentView.as_view(), name='patient-list'),



