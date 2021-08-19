from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.decorators import api_view, parser_classes
from drf_yasg.utils import swagger_auto_schema

from tryon.serializers import ProductNBSerializer, ProductSerializer
from tryon.models import ProductNB
from tryon.utils.path import get_static_img_path


@swagger_auto_schema(
    method='post',
    operation_id="Product Image Post",
    operation_description="Step2. 상품 이미지 업로드에 사용될 API, no background image가 반환됩니다.",
    request_body=ProductSerializer,
    responses={
        200: ProductNBSerializer,
        404: "Not Found",
    },
    tags=['Product']
)
@api_view(['POST'])
@parser_classes((MultiPartParser, FileUploadParser))
def product_image(request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    product = serializer.save()
    data = serializer.validated_data
    new_title = 'Fancy cloth for summer'
    nb_img = get_no_back_img(data['image'])
    nobg_post = ProductNB.objects.create(
        image=nb_img, part=data['part'], title=new_title, product=product)
    serializer = ProductNBSerializer(nobg_post)
    data = serializer.data
    data['image'] = get_static_img_path(data['image'])
    return JsonResponse(data, safe=False)


# Temp
def get_no_back_img(img):
    return img
