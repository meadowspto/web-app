from datetime import datetime

from django import forms
from django.core.management import call_command
from django.contrib.auth.models import User
from django.core.validators import validate_email

from .models import VolunteerSignup, NotificationSignup, Reservation

class NotificationSignupForm(forms.Form):
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'Please enter a valid email address.',
            'invalid': 'Please enter an email address',
            'exists': 'exists exists exists',
        },
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your email address',
                'class': 'form-control',
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']

        if NotificationSignup.email_exists(self.cleaned_data.get('email')) is True:
            raise forms.ValidationError('The email you entered is already signed up.')

        return email

    def save(self, commit=True):
        signup = NotificationSignup()
        signup.email = self.cleaned_data['email']

        if commit:
            signup.save()

        return signup

class VolunteerSignupForm(forms.Form):
    full_name = forms.EmailField(
        required=True,
        label='Full Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Full Name',
                'class': 'form-control',
                'ng-model': 'fullName',
            },
        )
    )

    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control',
                'ng-model': 'email',
            },
        )
    )

    def clean(self):
        print 'cleaningcleaningcleaningcleaningcleaningcleaningcleaningcleaningcleaningcleaning'

        if (len(self.cleaned_data.get('email')) == 0):
            raise ValidationError(
                'Please enter a valid email address.'
            )

        return self.cleaned_data

    def save(self, commit=True):
        print 'savingsavingsavingsavingsavingsavingsavingsavingsavingsavingsaving'

        signup = VolunteerSignup()
        signup.full_name = self.cleaned_data['full_name']
        signup.email = self.cleaned_data['email']

        # if commit:
        #     user.save()

        return signup

class CheckInForm(forms.Form):
    check_in_count = forms.CharField(
        required=True,
        widget=forms.HiddenInput(
            attrs={
                'value': '{[ checkInCount ]}',
            }
        )
    )

    reservation_id = forms.CharField(
        required=True,
        widget=forms.HiddenInput()
    )

    def save(self, commit=True):
        reservation = Reservation.objects.get(id=int(self.cleaned_data['reservation_id']))
        reservation.party_checked_in = reservation.party_checked_in + int(self.cleaned_data['check_in_count'])
        reservation.check_in_date = datetime.now()

        if commit:
            reservation.save()
            call_command('index_transactions')

        return reservation