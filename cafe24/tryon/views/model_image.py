from tryon.models import Model, Product, ProductNB, TemplatePage, TryOnImage
from django.http import HttpResponse, JsonResponse
from tryon.serializers import ModelSerializer, ProductSerializer, ProductNBSerializer, ADProductSerializer
import urllib.request

import os
from os.path import pjoin
import PIL
import ftplib

# 해당 파트는 성찬이 형의 모듈화 기다리는 중
from '' import TryOnGenerator, TitleGnerator
from '' import detect_bg, make_html


# Model Image BaseDir
MODELIMGDIR = '/home/hsna/workspaces/try-on/try_on_image_dir/models'

TOG = TryOnGenerator()
TG = TitleGnerator()

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


# access model_images
@api_view(['GET', 'POST'])
def model_image(request, id):
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

        file = request.data['file']
        post = Models.objects.create(image=file)
        return HttpResponse(status=200)


# id를 생성해 줘야 하나?
@api_view(['POST'])
def product_image(request):
    # return model images
    # add model images
    file = request.data['file']
    post = Product.objects.create(image=file)
    part = request.data['part']

    new_title = TG.gen_title(file)
    nobg_file = detect_bg(file)
    nobg_post = ProductNB.objects.create(image=nobg_file, part=part, title=new_title)

    serializer_class = ProductNBSerializer(nobg_post)

## return HttpResponse with image? 아니면 자체적으로 다른 걸?
    return JsonResponse(serializer_class.data, safe=False)


# is this page necessary?
@api_view(['GET'])
def detail_page(request):
    try:
        id = request.data['id']
        # post = Models.objects.filter(user_name=id)
        post = ProductNB.objects.get(id=id)
    except Models.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ModelSerializer(post, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def create_template(request):
    model_ids = request.data['model_ids']
    nobg = request.data['nobg_id']

    model_posts = Model.objects.filter(id=model_ids)
    nobg_post = ProductNB.objects.get(id=nobg)

    model_img_urls= model_posts.image.url
    nobg_img_url = nobg_post.image.url
    part = nobg_post.part
    title = nobg_post.title

    ftp = ftplib.FTP()
    ftp.retrlines('LIST')

    url_list = []
    for url in range(len(model_img_urls)):
        new_id = f'{nobg}_{model_ids[url]}.jpg'

        result=TOG.get_tryon(nobg_img_url, model_img_urls[url], part=part)
        img_result = TryOnImage.objects.create(image=result, title=title)
        new_url = f'STOR/web/{new_id}'
        url_list.append(new_url)

        ftp.storbinary(new_url, result)

    ftp.quit()

    htmls = make_html(url_list)
    templates = TemplatePage.objects.create(title=title, name=name, part=part,
                                            single_line=htmls[0],
                                            grid=htmls[1],
                                            zigzag=htmls[2]
                                            )

    return JsonResponse(htmls)


@api_view(['GET'])
def layout_page(request):
    try:
        id = request.data['id']
        # post = Models.objects.filter(user_name=id)
        post = TemplatePage.objects.get(name=name)
    except Models.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ModelSerializer(post)
    return JsonResponse(serializer.data, safe=False)


# TODO : 상품 가등록 page
@api_view(['POST'])
def register_page(request):
    return
