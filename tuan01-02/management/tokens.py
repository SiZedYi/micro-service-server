from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class CustomToken(RefreshToken):

    @classmethod
    def for_user(cls, user: User):
        token = super().for_user(user)

        return token

def create_jwt_pair_for_user(user: User):
    refresh = CustomToken.for_user(user)
    tokens = {"access": str(refresh.access_token), "refresh": str(refresh)}
    return tokens
