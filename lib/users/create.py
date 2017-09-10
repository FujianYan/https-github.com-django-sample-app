from django.contrib.auth.models import User


def create_user(username, password, email):
    """
    Create a new user by username, password and email.
    """
    user = User(
        username=username,
        email=email
    )
    user.set_password(password)
    user.save()
    return user
