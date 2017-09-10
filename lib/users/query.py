from django.contrib.auth.models import User


# TODO: will be deleted after formalizing registration logic
def get_all_users():
    """
    Get all users
    """
    return User.objects.all()


def get_user_by_email(email):
    """
    Get user by email
    """
    return User.objects.filter(email=email).first()
