import os
from pdb import set_trace
import requests
import json
from django.conf import settings
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.decorators import api_view, parser_classes
from drf_yasg.utils import swagger_auto_schema
from os.path import join as pjoin
from django.core.files import File

from tryon.services.try_on_back_modules.tryongenerator.utils.util_module import TryOnUtils
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
    utils = TryOnUtils()
    utils.pad_overall([product.image.path],
                      dest_dir=pjoin(settings.PRE_DIR, "cloth"))

    saved_path = utils.detect_bg(
        img_path=product.image.path, no_bg_dir=pjoin(settings.MEDIA_ROOT))

    saved_path_small = utils.detect_bg(
        img_path=pjoin(settings.PRE_DIR, "cloth", os.path.basename(product.image.name)), no_bg_dir=pjoin(settings.PRE_DIR))

    new_title = requests.post('http://127.0.0.1:8522',
                              data=json.dumps(saved_path)).json()

    nobg_post = ProductNB.objects.create(image=File(
        open(saved_path, "rb")), part=data['part'], title=new_title, product=product)

    utils.make_cloth_mask(img_path=saved_path_small, mask_dir=pjoin(
        settings.PRE_DIR, "cloth-mask"))

    os.remove(saved_path)
    os.remove(saved_path_small)

    serializer = ProductNBSerializer(nobg_post)
    data = serializer.data
    data['image'] = get_static_img_path(data['image'])
    return JsonResponse(data, safe=False)
