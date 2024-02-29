from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status

import pandas as pd
from management.serializers import ProductSerializer, UserSerializer
from management.models import User, Product
from management.utils.apicode import ApiCode


class ListProductView(generics.GenericAPIView):
    def post(self, request):
        product_id = request.data['product_id']
        user_obj = request.user
        # user_obj = User.objects.get(user_name=user_name)

        product_list = Product.objects.filter(product_id=product_id)
        serializer = ProductSerializer(product_list, many=True)

        return Response(data=ApiCode.success(
             data={"product_data": serializer.data,"user_name":user_obj.user_name}
        ), status=status.HTTP_200_OK)

