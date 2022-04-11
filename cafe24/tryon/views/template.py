import json
import os
import pdb
from tryon.services.try_on_back_modules.tryongenerator.utils.util_module import TryOnUtils
from tryon.serializers.template import TemplateModelSerializer, TemplatePostSerializer
from tryon.models import TryOnImage
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from django.core.files import File
import requests
from django.conf import settings
from os.path import join as pjoin

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
        p.image.name for p in Models.objects.filter(id__in=d['model_ids'])]
    user_info = get_user_info()
    imgdict_list = generate_tryon(
        nb_prod_path=nobg_post.image.path,
        product=nobg_post.product,
        model_imgs_path=model_imgs_path,
        user_info=user_info, )
    tryons = []
    for d in imgdict_list:
        if 'product' in d['dest']:
            nobg_post.url = get_ftp_img_url(
                shop_url=user_info['shop_url'], dest_url=d['dest'])
            nobg_post.save()
        elif 'model' in d['dest']:
            ftp_url = get_ftp_img_url(
                shop_url=user_info['shop_url'], dest_url=d['dest'])
            tryons.append(TryOnImage(name="", url=ftp_url, image=File(
                open(d['src'], 'rb')), default=False))
    tryon_imgs = TryOnImage.objects.bulk_create(tryons)
    unique_urls = set(map(lambda x: x.url, tryon_imgs))
    unique_imgs = set(map(lambda x: x.image, tryon_imgs))
    serializer = TryOnImageModelSerializer(
        TryOnImage.objects.filter(url__in=unique_urls, image__in=unique_imgs), many=True)
    for d in serializer.data:
        d['image'] = get_static_img_path(d['image'])
    return Response(data=serializer.data, status=status.HTTP_200_OK)


bottom_parts = ["하의", "반바지", "긴바지", "ShortPants", "LongPants"]


def generate_tryon(nb_prod_path, product, model_imgs_path, user_info):
    imgdict_list = []
    prod_path = product.image.name.replace(
        "products", pjoin(settings.PRE_DIR, "cloth"))
    mask_path = product.image.name.replace("products", pjoin(
        settings.PRE_DIR, "cloth-mask")).split(".")[0] + ".jpg"
    models_path = list(map(lambda p: p.replace("models", pjoin(
        settings.PRE_DIR, "image")).split(".")[0] + ".jpg", model_imgs_path))
    prod_name = os.path.basename(prod_path).split(".")[0]

    if product.part in bottom_parts:
        print("하의 모델 구동 Param: ", product.part)
        res = requests.post(url="http://127.0.0.1:8524", data=json.dumps({
            'dataroot': settings.PRE_DIR, 'models': models_path, 'cloth': prod_path
        }))

    else:
        print("상의 모델 구동 Param: ", product.part)
        res = requests.post(url="http://127.0.0.1:8523", data=json.dumps({
            "cloth": prod_path, "edge": mask_path, "models": models_path, "dest": pjoin(settings.PRE_DIR, "tryon", prod_name)
        }))

    try_img_path_list = res.json()
    for i in try_img_path_list:
        imgdict_list.append(
            {"src": i, "dest": f'models/{os.path.basename(nb_prod_path).split(".")[0]}/{os.path.basename(i)}'})
    imgdict_list.append(
        {"src": nb_prod_path, "dest": f'products/{os.path.basename(nb_prod_path)}'})
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
    utils = TryOnUtils()
    htmls = utils.make_html(img_urls=list(
        map(lambda x: "http://" + x, model_urls)))
    template = TemplatePage.objects.create(
        name="test", title="test", part="test", **htmls)
    return Response(data=TemplateModelSerializer(template).data, status=status.HTTP_200_OK)
