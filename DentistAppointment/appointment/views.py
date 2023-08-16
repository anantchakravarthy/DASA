
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from accounts.models import User
from accounts.views import user_is_dentist
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, DetailView, DeleteView
from django.views.generic.edit import DeleteView, UpdateView
from .forms import TakeAppointmentForm, CreateAppointmentForm, CreateLogForm
from .models import Appointment, DentistLog


class ServiceView(TemplateView):
    template_name = 'appointment/service.html'


class TakeAppointmentView(CreateView):
    template_name = 'appointment/take_appointment.html'
    form_class = TakeAppointmentForm
    extra_context = {
        'title': 'Take Appointment'
    }
    success_url = reverse_lazy('accounts:home')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if self.request.user.is_authenticated and self.request.user.role != 'patient':
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TakeAppointmentView, self).form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)


class CreateAppointmentView(CreateView):
    template_name = 'appointment/create_appointment.html'
    form_class = CreateAppointmentForm
    extra_context = {
        'title': 'Create Appointment'
    }
    success_url = reverse_lazy('accounts:home')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if self.request.user.is_authenticated and self.request.user.role != 'dentist':
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.dentist = self.request.user
        return super(CreateAppointmentView, self).form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointment/appointment.html'
    context_object_name = 'appointment'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.role == 'dentist':
            return self.model.objects.filter(dentist=self.request.user.id).order_by('-created_at')
        elif self.request.user.role == 'patient':
            return self.model.objects.filter(user=self.request.user.id).order_by('-created_at')

class AppointmentDeleteView(DeleteView):
    """
       For Delete any Appointment created by Doctor
    """
    model = Appointment
    success_url = reverse_lazy('appointment:my-appointments')


class CreateLogView(CreateView):
    template_name = 'appointment/create_log.html'
    form_class = CreateLogForm
    extra_context = {
        'title': 'Create Log'
    }
    success_url = reverse_lazy('accounts:home')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('accounts:login')
        if self.request.user.is_authenticated and self.request.user.role != 'dentist':
            return reverse_lazy('accounts:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.appointment = Appointment.objects.get(pk=self.kwargs['pk'])
        return super(CreateLogView, self).form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)

class LogListView(ListView):
    model = DentistLog
    template_name = 'appointment/log.html'
    context_object_name = 'dentistlog'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_dentist)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(appointment=self.kwargs['pk']).order_by('-created_at')

class PatientDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy('appointment:patient-list')



"""
   For both Profile
   
"""


class HomePageView(ListView):
    paginate_by = 9
    model = Appointment
    context_object_name = 'home'
    template_name = "home.html"

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')



class ServiceView(TemplateView):
    template_name = 'appointment/service.html'

class SearchView(ListView):
    paginate_by = 6
    model = Appointment
    template_name = 'appointment/search.html'
    context_object_name = 'appointment'

    




