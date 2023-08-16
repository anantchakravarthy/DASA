from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password

from accounts.models import User

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('not to disclose', 'Not To Disclose'))


class PatientRegistrationForm(UserCreationForm):
    #gender = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=GENDER_CHOICES)

    def __init__(self, *args, **kwargs):
        super(PatientRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['gender'].required = True
        self.fields['username'].label = "Username"
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['email'].label = "Email"
        self.fields['phonenumber'].label = "Phone Number"
        self.fields['age'].label = "Age"
        self.fields['street'].label = "Street"
        self.fields['city'].label = "City"
        self.fields['state'].label = "State"
        self.fields['zipcode'].label = "Zipcode"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
            

        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'Enter Username',
            }
        )
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['phonenumber'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone Number',
            }
        )
        self.fields['age'].widget.attrs.update(
            {
                'placeholder': 'Enter your Age',
            }
        )
        self.fields['street'].widget.attrs.update(
            {
                'placeholder': 'Enter your Street Address',
            }
        )
        self.fields['city'].widget.attrs.update(
            {
                'placeholder': 'Enter your City',
            }
        )
        self.fields['state'].widget.attrs.update(
            {
                'placeholder': 'Enter your State',
            }
        )
        self.fields['zipcode'].widget.attrs.update(
            {
                'placeholder': 'Enter your Zipcode',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'phonenumber', 'age', 'street', 'city', 'state', 'zipcode', 'password1', 'password2', 'gender' ]
        error_messages = {
            'username': {
                'required': 'username is required',
                'max_length': 'Name is too long'
            },
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            },
            'gender': {
                'required': 'Gender is required'
            },
            'email': {
                'required': 'Email is required'
            },
            'password1': {
                'required': 'Password is required',
                'min_digits': 'Password must contain minimum of 4 digits',
                'min_uppercase': 'Password must contain minimum of 2 Upper Case Letter',
                'min_lowercase': 'Password must contain minimum of 2 Lower Case Letter',
                'min_characters': 'Password must contain minimum of 1 Special Character',
                'max_consecutive': 'Password must contain maximum of 3 Consective Characters/Increasing/Decreasing Digits',
                
            },
            'password2': {
                'required': 'Confirm Pasword action is required',
                
                
            },
            
        }

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "patient"
        if commit:
            user.save()
        return user


class DentistRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(DentistRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['gender'].required = True
        self.fields['username'].label = "Username"
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['email'].label = "Email"
        self.fields['phonenumber'].label = "Phone Number"
        self.fields['age'].label = "Age"
        self.fields['street'].label = "Street"
        self.fields['city'].label = "City"
        self.fields['state'].label = "State"
        self.fields['zipcode'].label = "Zipcode"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'Enter Username',
            }
        )
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['phonenumber'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone Number',
            }
        )
        self.fields['age'].widget.attrs.update(
            {
                'placeholder': 'Enter your Age',
            }
        )
        self.fields['street'].widget.attrs.update(
            {
                'placeholder': 'Enter your Street Address',
            }
        )
        self.fields['city'].widget.attrs.update(
            {
                'placeholder': 'Enter your City',
            }
        )
        self.fields['state'].widget.attrs.update(
            {
                'placeholder': 'Enter your State',
            }
        )
        self.fields['zipcode'].widget.attrs.update(
            {
                'placeholder': 'Enter your Zipcode',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phonenumber', 'age', 'street', 'city', 'state', 'zipcode', 'password1', 'password2', 'gender' ]
        error_messages = {
            'username': {
                'required': 'username is required',
                'max_length': 'Name is too long'
            },
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            },
            'gender': {
                'required': 'Gender is required'
            },
             'email': {
                'required': 'Email is required'
            },
            'password1': {
                'required': 'Password is required',
                'min_digits': 'Password must contain minimum of 4 digits',
                'min_uppercase': 'Password must contain minimum of 2 Upper Case Letter',
                'min_lowercase': 'Password must contain minimum of 2 Lower Case Letter',
                'min_characters': 'Password must contain minimum of 1 Special Character',
                'max_consecutive': 'Password must contain maximum of 3 Consective Characters/Increasing/Decreasing Digits',
                
            },
            'password2': {
                'required': 'Confirm Pasword action is required',
                
                
            },
            
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "dentist"
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password'})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("User Does Not Exist.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not self.user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


class PatientProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PatientProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Email',
            }
        )
        self.fields['phonenumber'].widget.attrs.update(
            {
                'placeholder': 'Phone Number',
            }
        )
        self.fields['age'].widget.attrs.update(
            {
                'placeholder': 'Enter your Age',
            }
        )
        self.fields['street'].widget.attrs.update(
            {
                'placeholder': 'Enter your Street Address',
            }
        )
        self.fields['city'].widget.attrs.update(
            {
                'placeholder': 'Enter your City',
            }
        )
        self.fields['state'].widget.attrs.update(
            {
                'placeholder': 'Enter your State',
            }
        )
        self.fields['zipcode'].widget.attrs.update(
            {
                'placeholder': 'Enter your Zipcode',
            }
        )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phonenumber", "street", "city", "state", "zipcode"]


class DentistProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DentistProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Email',
            }
        )
        self.fields['age'].widget.attrs.update(
            {
                'placeholder': 'Age',
            }
        )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "age"]