from tryon.serializers.template import TemplateModelSerializer, TemplatePostSerializer
from tryon.models import TryOnImage
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from django.core.files import File

from tryon.serializers import GenTryOnSerializer, TryOnImageModelSerializer
from tryon.models import Models, ProductNB, TemplatePage
from tryon.services.cafe.tryon_ftp import get_ftp_img_url, send_image_ftp, get_user_info
from tryon.utils.path import get_static_img_path


@swagger_auto_schema(
    method='post',
    operation_id="gen_tryon_models",
    operation_description="Step3. 상세 페이지 생성에서 사용되는 API, TryOn 모델을 반환합니다",
    request_body=GenTryOnSerializer,
    responses={
        200: TryOnImageModelSerializer(many=True),
        404: "Not Found",
    },
    tags=['Template']
)
@api_view(['POST'])
def gen_tryon_models(request):
    serializer = GenTryOnSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    d = serializer.validated_data

    nobg_post = ProductNB.objects.get(id=d['nobg_id'])
    model_imgs_path = [
        p.image.path for p in Models.objects.filter(id__in=d['model_ids'])]
    nobg_img_path = nobg_post.image.path
    user_info = get_user_info()
    imgdict_list = generate_tryon(
        prodnb_img_path=nobg_img_path, model_imgs_path=model_imgs_path, user_info=user_info)
    tryons = []
    for d in imgdict_list:
        if 'product' in d['dest']:
            nobg_post.url = get_ftp_img_url(
                shop_url=user_info['shop_url'], dest_url=d['dest'])
            nobg_post.save()
        elif 'model' in d['src']:
            ftp_url = get_ftp_img_url(
                shop_url=user_info['shop_url'], dest_url=d['dest'])
            tryons.append(TryOnImage(name="", url=ftp_url, image=File(
                open(d['src'], 'rb')), default=False))
    tryon_imgs = TryOnImage.objects.bulk_create(tryons)
    unique_urls = set(map(lambda x: x.url, tryon_imgs))
    serializer = TryOnImageModelSerializer(
        TryOnImage.objects.filter(url__in=unique_urls), many=True)
    for d in serializer.data:
        d['image'] = get_static_img_path(d['image'])
    return Response(data=serializer.data, status=status.HTTP_200_OK)


def generate_tryon(prodnb_img_path, model_imgs_path, user_info):
    imgdict_list = []
    for i in model_imgs_path:
        imgdict_list.append({"src": i, "dest": f'models/{i.split("/")[-1]}'})
    imgdict_list.append(
        {"src": prodnb_img_path, "dest": f'products/{prodnb_img_path.split("/")[-1]}'})
    send_image_ftp(imgdict_list, **user_info)
    return imgdict_list


@swagger_auto_schema(
    method='post',
    operation_id="create_template",
    operation_description="Step3. 상세 페이지 생성에서 사용되는 API",
    request_body=TemplatePostSerializer,
    responses={
        200: TemplateModelSerializer,
        404: "Not Found",
    },
    tags=['Template']
)
@api_view(['POST'])
def create_template(request):
    serializer = TemplatePostSerializer(data=request.data)
    serializer.is_valid(True)
    d = serializer.validated_data
    model_urls = TryOnImage.objects.filter(
        pk__in=d['tryon_ids']).values_list("url", flat=True)
    htmls = make_html(image_urls=model_urls)
    template = TemplatePage.objects.create(
        name="test", title="test", part="test", **htmls)
    return Response(data=TemplateModelSerializer(template).data, status=status.HTTP_200_OK)


def make_html(image_urls):
    return {
        "single_line": "<h1> Single line </ h1>",
        "grid": "<h2> Grid </ h2>",
        "zigzag": "<h3> ZigZag </ h3>",
    }
