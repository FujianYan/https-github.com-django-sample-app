from django.db.models import Q
from django.contrib.auth.models import User


def is_user_id_valid(user_id):
    """
    Check if user exists given user_id
    """
    return User.objects.filter(id=user_id).exists()


def is_user_already_registered(username, email):
    """
    Check if username and email has been used.
    """
    return User.objects.filter(Q(email=email) | Q(username=username)).exists()
