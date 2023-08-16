from django.contrib.auth import views as auth_views
from django.urls import include, path, reverse_lazy
from defender import utils
from .views import *

app_name='accounts'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    path('patient/register/', RegisterPatientView.as_view(), name='patient-register'),
    path('patient/profile/update/', EditPatientProfileView.as_view(), name='patient-profile-update'),
    
    path('dentist/register/', RegisterDentistView.as_view(), name='dentist-register'),
    path('dentist/profile/update/', EditDentistProfileView.as_view(), name='dentist-profile-update'),
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            success_url=reverse_lazy('accounts:password_reset_done')),
        name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),

    path('password_reset_<uidb64>_<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url=reverse_lazy('accounts:password_reset_complete')),
        name='password_reset_confirm'),
    
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
    
    # path('defender_lockout/', defender_views.UserLockoutView.as_view(
    #         template_name='accounts/defender_lockout.html'),
    #     name='defender_lockout'),
    
]