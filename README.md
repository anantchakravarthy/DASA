Dentist appointment application using django

create virtual environment:
python3 -m venv demoenv

activate virtual environment:
source demoenv/bin/activate

create project:
django-admin startproject dentistappointment

install requirements.txt file

python commands:
python manage.py makemigrations  #this creates migration files
python manage.py migrate         #this applies migrations to db
python manage.py runserver       #to run the project


create apps:
python manage.py startapp accounts
create urls.py, forms.py, managers.py file inside accounts folder
python manage.py startapp appointment
create urls.py, forms.py inside accounts folder



changes to be made in settings.py file

AUTH_USER_MODEL = 'accounts.User'

append created apps and installed packages inside INSTALLED_APPS list
INSTALLED_APPS = [
    .....,
    .....,
    'whitenoise.runserver_nostatic',
    'bootstrapform',
    'accounts',
    'appointment',
    "verify_email.apps.VerifyEmailConfig",
    'django_advanced_password_validation',
    'defender',
]

append this to MIDDLEWARE list
MIDDLEWARE = [
    ......,
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'csp.middleware.CSPMiddleware',
    'defender.middleware.FailedLoginMiddleware',
]

alter 'DIRS': [] in TEMPLATES list as:
'DIRS': [BASE_DIR /'templates']

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_DIR = BASE_DIR / "media",
MEDIA_ROOT = BASE_DIR / "media",
MEDIA_URL = "/media/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your email address'
EMAIL_HOST_PASSWORD = 'app-password for the email entered'

DEFAULT_FROM_EMAIL = 'noreply<no_reply@domain.com>'


changes to be made in django template for password reset flow:

demoenv > lib > python3 > sie-packages > django > contrib > admin > templates > registration > password_reset_email.html file line no.6 replace 'url 'password_reset_confirm'with url 'accounts:password_reset_confirm'

after running pyton manage.py runserver you would successfully recieve the development url http://127.0.0.1:8000/ due to implementation of ssl aand and secure cookies it would provide an error. in such a scenario in the url space type localhost:8000 and it will allow you to the application.

 python -m pip install django[argon2] for installing argon 2 libraries and config file
 use the link https://docs.djangoproject.com/en/4.1/topics/auth/passwords/ for more information

 sometimes the created_at and date fields in models.py of appointment might pose errors in rendering my appointment page in such a case change it it from 

 date = models.DateField(default=date.today)
 created_at = models.DateTimeField(default=timezone.now)

 to
 date = models.DateTimeField(default=date.today)
 created_at = models.DateTimeField(default=timezone.now)


 