from tryon.models import Models, Product, ProductNB, TemplatePage, TryOnImage
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.decorators import api_view, parser_classes
from tryon.serializers import ModelSerializer, ProductSerializer, ProductNBSerializer, TemplateSerializer, TemplatePostSerializer, RegisterTemplateSerializer
from tryon.views.file_maker import make_html
from drf_yasg.utils import swagger_auto_schema

import urllib.request
import os
from os.path import join as pjoin
from django.core.files import File
import ftplib

# TODO : 해당 파트는 성찬이 형의 모듈화 기다리는 중
# from '' import TryOnGenerator, TitleGnerator
# from '' import detect_bg, make_html
# TOG = TryOnGenerator()
# TG = TitleGnerator()

# Model Image BaseDir
MODELIMGDIR = '/home/hsna/workspaces/try-on/try_on_image_dir/models'

'''
    ViewSet과 일반 중에 어떤 게 좋을지 고민 중 
'''

# @api_view(['GET', 'POST'])
# class ModelViewSet(ListAPIView):
#     queryset = Model.objects.all()
#     serializer_class = ModelSerializer
#
#     def post(self, request, *args, **kwargs):
#         file = request.data['file']
#         image = Model.objects.create(image=file)
#         return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)
#
#     def get(self, request):
#         return JsonResponse(serializer_class.data, safe=False)
#
#
# @api_view(['GET', 'POST'])
# class ProductViewSet(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def post(self, request, *args, **kwargs):
#         file = request.data['file']
#         part = request.data['part']
#         image = Product.objects.create(image=file)
#         return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

################################################

@swagger_auto_schema(
    method='get',
    operation_id="Model Image View Get",
    operation_description="Provide Model Images",
    responses={
        200: ModelSerializer,
        404: "Not Found",
    },
    tags=['Model']
)

@swagger_auto_schema(
    method='post',
    operation_id="Model Image View Post",
    operation_description="Save Model Images",
    request_body=ModelSerializer,
    responses={
        200: "Good",
        404: "Not Found",
    },
    tags=['Model']
)

# access model_images
@api_view(['GET', 'POST'])
@parser_classes((MultiPartParser, FileUploadParser))
def model_image(request):
    # return model images
    if request.method == 'GET':
        try:
            # post = Models.objects.filter(user_name=id)
            post = Models.objects.all()
        except Models.DoesNotExist:
            return HttpResponse(status=404)

        serializer = ModelSerializer(post, many=True)
        return JsonResponse(serializer.data, safe=False)

    # add model images
    elif request.method == 'POST':
        serializer = ModelSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return HttpResponse(status=200)

@swagger_auto_schema(
    method='post',
    operation_id="Product Image Post",
    operation_description="Save Product Images",
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

    # TODO : Reset after module is done
    # new_title = TG.gen_title(file)
    # nobg_file = detect_bg(file)

    new_title = 'Fancy cloth for summer'
    nobg_file = File(open('/data/try-on-image-dir/background_crop/product_4.jpg', "rb"))
    nobg_post = ProductNB.objects.create(
        image=nobg_file, part=data['part'], title=new_title, product=product)
    serializer = ProductNBSerializer(nobg_post)

    return JsonResponse(serializer.data, safe=False)


@swagger_auto_schema(
    method='get',
    operation_id="Detail Image View Post",
    operation_description="Save Detail Images",
    responses={
        200: ProductNBSerializer,
        404: "Not Found",
    },
    tags=['Detail']
)

# is this page necessary?
@api_view(['GET'])
def detail_page(request):
    try:
        id = request.data['id']
        # post = Models.objects.filter(user_name=id)
        post = ProductNB.objects.get(id=id)
    except Models.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ProductNBSerializer(post)
    return JsonResponse(serializer.data, safe=False)


@swagger_auto_schema(
    method='post',
    operation_id="Template Post",
    operation_description="Create Templates",
    request_body=TemplatePostSerializer,
    responses={
        200: TemplateSerializer,
        404: "Not Found",
    },
    tags=['Template']
)

# Create Detail Page
@api_view(['POST'])
def create_template(request):
    serializer = TemplatePostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    d = serializer.data
    model_posts = Models.objects.filter(id__in=d['model_ids'])
    nobg_post = ProductNB.objects.get(id=d['nobg_id'])
    model_img_urls= [p.image.url for p in model_posts]
    nobg_img_url = nobg_post.image.url
    part = nobg_post.part
    title = nobg_post.title

    ftp= ftplib.FTP('tjagksro.cafe24.com','tjagksro','Fitzme123!@')
    ftp.retrlines('LIST')

    url_list = []
    for url in range(len(model_img_urls)):
        new_id = f"{d['nobg_id']}__{'_'.join(map(str, d['model_ids']))}.jpg"

        # result=TOG.get_tryon(nobg_img_url, model_img_urls[url], part=part)
        # img_result = TryOnImage.objects.create(image=result, title=title)
        new_url = f'STOR/web/{new_id}'
        url_list.append(new_url)

        # ftp.storbinary(new_url, result)

    ftp.quit()

    htmls = make_html(url_list)
    templates = TemplatePage.objects.create(title=title, name='name', part=part,
                                            single_line=htmls[0],
                                            grid=htmls[1],
                                            zigzag=htmls[2]
                                            )

    serializer_class = TemplateSerializer(templates)

    return JsonResponse(serializer_class.data, safe=False)

@swagger_auto_schema(
    method='get',
    operation_id="Template Format Get",
    operation_description="Provide Html Template format",
    responses={
        200: TemplateSerializer,
        404: "Not Found",
    },
    tags=['Template']
)

# TODO : Is this function necessary?
@api_view(['GET'])
def layout_page(request):
    try:
        id = request.data['id']
        # post = Models.objects.filter(user_name=id)
        post = TemplatePage.objects.get(name=name)
    except Models.DoesNotExist:
        return HttpResponse(status=404)

    serializer = TemplateSerializer(post)
    return JsonResponse(serializer.data, safe=False)

@swagger_auto_schema(
    method='post',
    operation_id="Page Generation Post",
    operation_description="Generate Product Page",
    request_body=RegisterTemplateSerializer,
    responses={
        200: "Good",
        404: "Not Found",
    },
    tags=['Register']
)

# TODO : 상품 가등록 page
@api_view(['POST'])
def register_page(request):
    try:
        serializer = RegisterTemplateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # post = Models.objects.filter(user_name=id)
        return HttpResponse(status=200)
    except Models.DoesNotExist:
        return HttpResponse(status=404)
