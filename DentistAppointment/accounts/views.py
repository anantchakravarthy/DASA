from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from accounts.models import User
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, DetailView, DeleteView, FormView, RedirectView
from django.views.generic.edit import DeleteView, UpdateView
from accounts.forms import *
from django.core.exceptions import PermissionDenied
from django.contrib.auth.password_validation import validate_password
from defender import utils as def_utils
from django.contrib.auth import views as auth_views

def user_is_patient(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'patient':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap


def user_is_dentist(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'dentist':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

class HomePageView(TemplateView):
    template_name = 'home.html'


class RegisterPatientView(CreateView):
    """
        Provides the ability to register as a Patient.
    """
    model = User
    form_class = PatientRegistrationForm
    template_name = 'accounts/patient/register.html'
    success_url = '/'

    extra_context = {
        'title': 'Register'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/patient/register.html', {'form': form})


class EditPatientProfileView(UpdateView):
    model = User
    form_class = PatientProfileUpdateForm
    context_object_name = 'patient'
    template_name = 'accounts/patient/edit-profile.html'
    success_url = reverse_lazy('accounts:home')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_patient)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        if obj is None:
            raise Http404("Patient doesn't exists")
        return obj


class RegisterDentistView(CreateView):
    """
       Provides the ability to register as a Dentist.
    """
    model = User
    form_class = DentistRegistrationForm
    template_name = 'accounts/dentist/register.html'
    success_url = '/'

    extra_context = {
        'title': 'Register'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/dentist/register.html', {'form': form})


class EditDentistProfileView(UpdateView):
    model = User
    form_class = DentistProfileUpdateForm
    context_object_name = 'dentist'
    template_name = 'accounts/dentist/edit-profile.html'
    success_url = reverse_lazy('accounts:home')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_dentist)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        if obj is None:
            raise Http404("Dentist doesn't exists")
        return obj


class LoginView(FormView):
    """
        Provides the ability to login as a user with an email and password
    """
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    extra_context = {
        'title': 'Login'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):
    """
        Provides users the ability to logout
    """
    url = '/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)
    

class PasswordResetBruteForceProtectedView(auth_views.PasswordResetView):
    def get(self, request, *args, **kwargs):
        """Confirm the user isn’t already blocked by IP before showing the password reset view."""
        if def_utils.is_already_locked(request):
            return def_utils.lockout_response(request)
        return super(PasswordResetBruteForceProtectedView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Confirm the user isn’t already blocked by IP before allowing form POST.

        Also, force log this form POST as a single entry in the Defender cache, against the submitted email address.
        """
        if def_utils.is_already_locked(request):
            return def_utils.lockout_response(request)
        def_utils.check_request(
            request, login_unsuccessful=True, username=request.POST.get("email")
        )
        return super().post(request, *args, **kwargs)

# #defender
# class PasswordResetConfirmBruceForceProtectedView(auth_views.PasswordResetConfirmView):
#     def get(self, request, *args, **kwargs):
#         """Confirm the user isn’t already blocked by IP before showing the password confirm view."""
#         if def_utils.is_already_locked(request):
#             return def_utils.lockout_response(request)
#         return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         """Confirm the user isn’t already blocked by IP before allowing form POST for the password change confirmation."""
#         if def_utils.is_already_locked(request):
#             return def_utils.lockout_response(request)
#         return super().post(request, *args, **kwargs)

#     def form_valid(self, form):
#         """Force clear all the cached Defender statues for the user’s email address after successfully changing their password."""
#         super_valid = super().form_valid(form)
#         def_utils.check_request(
#             self.request, login_unsuccessful=False, username=self.user.email
#         )
#         return super_valid
