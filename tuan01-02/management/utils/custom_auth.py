from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomAdminLoginBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(user_name=username)
            # Add your custom authentication logic here
            if user and user.is_staff and user.password == password:
                return user
        except User.DoesNotExist:
            return None
