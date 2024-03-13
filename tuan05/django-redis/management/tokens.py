from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.response import Response
from rest_framework import status
User = get_user_model()

class CustomToken(RefreshToken):

    @classmethod
    def for_user(cls, user: User):
        token = super().for_user(user)
        # Add is_manager field to both access and refresh tokens
        token.payload["is_manager"] = user.is_manager

        access_token = token.access_token
        access_token.payload["is_manager"] = user.is_manager
        return token

def create_jwt_pair_for_user(user: User):
    refresh = CustomToken.for_user(user)
    tokens = {"access": str(refresh.access_token), "refresh": str(refresh)}
    return tokens


#  Decorator tùy chỉnh để kiểm tra token JWT của người dùng
def jwt_required(function):
    """
    Decorator for views that checks if the user is authenticated with a JWT token.
    """
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "Bạn cần đăng nhập để sử dụng chức năng này"},
                            status=status.HTTP_401_UNAUTHORIZED)
        return function(request, *args, **kwargs)
    return wrapper
