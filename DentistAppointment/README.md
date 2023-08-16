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
EMAIL_HOST_PASSWORD = 'password'

DEFAULT_FROM_EMAIL = 'noreply<no_reply@domain.com>'


changes to be made in django template for password reset flow:

demoenv > lib > python3 > sie-packages > django > contrib > admin > templates > registration > password_reset_email.html file line no.6 replace 'url 'password_reset_confirm'with url 'accounts:password_reset_confirm'

