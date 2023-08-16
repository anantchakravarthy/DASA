from django import forms
from .models import Appointment, DentistLog
from accounts.models import User


time_widget = forms.widgets.TimeInput(attrs={'class': 'time-pick'})
valid_time_formats = ['%I:%M %p',]

class TakeAppointmentForm(forms.ModelForm):

    # start_time = forms.TimeField(widget=time_widget, input_formats=valid_time_formats)
    # end_time = forms.TimeField(widget=time_widget, input_formats=valid_time_formats)

    def __init__(self, *args, **kwargs):
        super(TakeAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['dentist'].label = "Choose Your Dentist"
        self.fields['dentist'].queryset = User.objects.filter(role='dentist')
        self.fields['reason'].label = "Reason for appointment"
        self.fields['date'].label = "Date of Appointment"
        self.fields['start_time'].label = "Start Time"
        self.fields['end_time'].label = "End Time"
        self.fields['message'].label = "Message"

        self.fields['dentist'].widget.attrs.update(
            {
                'placeholder': 'Choose Your Dentist',
            }
        )

        self.fields['reason'].widget.attrs.update(
            {
                'placeholder': 'Choose Your Reason',
            }
        )

        self.fields['date'].widget.attrs.update(
            {
                'placeholder': 'Enter Date of Appointment',
            }
        )

        self.fields['start_time'].widget.attrs.update(
            {
                'placeholder': 'Ex: 11:00 AM',
            }
        )

        self.fields['end_time'].widget.attrs.update(
            {
               'placeholder': 'Ex: 12:00 PM',
            }
        )

        self.fields['message'].widget.attrs.update(
            {
                'placeholder': 'Write a short message',
            }
        )

    class Meta:
        model = Appointment
        fields = ['dentist', 'reason', 'date', 'start_time', 'end_time', 'message']

    def is_valid(self):
        valid = super(TakeAppointmentForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(TakeAppointmentForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment


class CreateAppointmentForm(forms.ModelForm):

    # start_time = forms.TimeField(widget=time_widget, input_formats=valid_time_formats)
    # end_time = forms.TimeField(widget=time_widget, input_formats=valid_time_formats)

    def __init__(self, *args, **kwargs):
        super(CreateAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['user'].label = "Choose Your Patient"
        self.fields['user'].queryset = User.objects.filter(role='patient')
        self.fields['reason'].label = "Reason for appointment"
        self.fields['date'].label = "Date of Appointment"
        self.fields['start_time'].label = "Start Time"
        self.fields['end_time'].label = "End Time"
        self.fields['message'].label = "Message"

        self.fields['user'].widget.attrs.update(
            {
                'placeholder': 'Choose Your Patient',
            }
        )

        self.fields['reason'].widget.attrs.update(
            {
                'placeholder': 'Choose Your Reason',
            }
        )

        self.fields['date'].widget.attrs.update(
            {
                'placeholder': 'Enter Date of Appointment',
            }
        )

        self.fields['start_time'].widget.attrs.update(
            {
                'placeholder': 'Ex: 11:00 AM',
            }
        )

        self.fields['end_time'].widget.attrs.update(
            {
               'placeholder': 'Ex: 12:00 PM',
            }
        )

        self.fields['message'].widget.attrs.update(
            {
                'placeholder': 'Write a short message',
            }
        )

    class Meta:
        model = Appointment
        fields = ['user', 'reason', 'date', 'start_time', 'end_time', 'message']

    def is_valid(self):
        valid = super(CreateAppointmentForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(CreateAppointmentForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment


class CreateLogForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateLogForm, self).__init__(*args, **kwargs)
        self.fields['consultation_date'].label = "Consultation Date"
        self.fields['consultation_duration'].label = "Duration"
        self.fields['consultation_details'].label = "Details"
        
        self.fields['consultation_date'].widget.attrs.update(
            {
                'placeholder': 'Date of Consultation',
            }
        )

        self.fields['consultation_duration'].widget.attrs.update(
            {
                'placeholder': 'Duration of Consultation',
            }
        )

        self.fields['consultation_details'].widget.attrs.update(
            {
                'placeholder': 'Enter Details',
            }
        )

    class Meta:
        model = DentistLog
        fields = ['consultation_date', 'consultation_duration', 'consultation_details']

    def is_valid(self):
        valid = super(CreateLogForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        appointment = super(CreateLogForm, self).save(commit=False)
        if commit:
            appointment.save()
        return appointment
