import json
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status

from management.models.user import User
from management.serializers.user import UserSerializer
from management.utils.apicode import ApiCode
from management.tokens import create_jwt_pair_for_user
# Create your views here.

class RegisterView(generics.GenericAPIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=ApiCode.success(data=serializer.data), status=status.HTTP_201_CREATED)
        else:
            # Handle the case where the data is not valid
            return Response(ApiCode.error(data=serializer.errors), status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    def post(self, request):
        user_name = request.data['user_name']
        password = request.data['password']

        user = User.objects.filter(user_name=user_name).first()

        if user is None:
            raise AuthenticationFailed('Không tìm thấy tài khoản')

        if not user.check_password(password):
            raise AuthenticationFailed('Sai mật khẩu')

        tokens = create_jwt_pair_for_user(user)

        response = { "tokens": tokens }

        return Response(data=ApiCode.success(data=response, message="Login Successful"), status=status.HTTP_200_OK)