from django.core.exceptions import PermissionDenied


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