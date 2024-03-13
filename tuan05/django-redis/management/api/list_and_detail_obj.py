from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status

from management.serializers import ProductSerializer, UserSerializer
from management.models import User, Product
from management.utils.apicode import ApiCode
from management.tokens import jwt_required
from management.utils.perms import IsAdminUser

from django.utils.decorators import method_decorator
from django.core.cache import cache

def get_product_from_redis():
    # Lấy dữ liệu của key PRODUCT
    cached_data = cache.get('PRODUCT')

    # Kiểm tra dữ liệu của key PRODUCT nếu có thì trả ra Response
    if cached_data:
        print("Dữ liệu đã được cache:", cached_data)
        return cached_data
    else:
        print("Dữ liệu chưa được cache.")
        # Lấy danh sách sản phẩm từ cơ sở dữ liệu
        product_list = Product.objects.all()
        serializer = ProductSerializer(product_list, many=True)

        # Lưu dữ liệu vào cache với key là 'PRODUCT'
        cache.set('PRODUCT', serializer.data, timeout=60 * 5)
        return serializer.data


def update_cache(instance):
    # Lấy danh sách sản phẩm từ cache
    cached_data = cache.get('PRODUCT')

    if cached_data:
        # Thêm sản phẩm mới vào danh sách cache
        cached_data.append(ProductSerializer(instance).data)

        # Lưu dữ liệu vào cache với key là 'PRODUCT'
        cache.set('PRODUCT', cached_data, timeout=60 * 5)

class ListProductView(generics.GenericAPIView):
    #Tất cả API từ class này sẽ được cache trong vòng 5 phút

    @method_decorator(jwt_required)
    def get(self, request, *args, **kwargs):
        product_data = get_product_from_redis()

        return Response(data=ApiCode.success(
                data=product_data
        ), status=status.HTTP_200_OK)

class GetProductByIdView(generics.GenericAPIView):
    def post(self, request):
        product_id = request.data['product_id']
        user_obj = request.user
        # user_obj = User.objects.get(user_name=user_name)

        product_list = Product.objects.filter(product_id=product_id)
        serializer = ProductSerializer(product_list, many=True)

        return Response(data=ApiCode.success(
             data={"product_data": serializer.data,"user_name":user_obj.user_name}
        ), status=status.HTTP_200_OK)

class CreateProductView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    # Chỉ có admin mới được thêm sản phẩm mới
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()
        update_cache(serializer.instance)

