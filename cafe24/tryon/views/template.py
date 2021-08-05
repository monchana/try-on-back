
from os.path import join as pjoin
from random import choice
import os
import ftplib
from django.http import JsonResponse
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

from tryon.serializers import TemplatePostSerializer, TemplateSerializer
from tryon.models import Models, ProductNB


def send_image_ftp(images, shop_url, nickname, pwd):
    ftp = ftplib.FTP()
    ftp.retrlines('LIST')
    file_path = '~/data/try-on-image-dir/products/'
    for image in images:
        file = open(pjoin(file_path, choice(os.listdir(file_path))), "rb")
        ftp.storbinary(f'STOR/web/{image}', file)

    ftp.quit()


def make_html(images):
    return (
        "<h1> Single line </ h1>",
        "<h2> Grid </ h2>",
        "<h3> ZigZag </ h3>",
    )


@swagger_auto_schema(
    method='post',
    operation_id="Template Post",
    operation_description="Step3. 상세 페이지 생성에서 사용되는 API",
    request_body=TemplatePostSerializer,
    responses={
        200: TemplateSerializer,
        404: "Not Found",
    },
    tags=['Template']
)
@api_view(['POST'])
def create_template(request):
    serializer = TemplatePostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    d = serializer.data
    model_posts = Models.objects.filter(id__in=d['model_ids'])
    nobg_post = ProductNB.objects.get(id=d['nobg_id'])
    model_img_urls = [p.image.url for p in model_posts]
    # nobg_img_url = nobg_post.image.url
    part = nobg_post.part
    title = nobg_post.title

    # ftp= ftplib.FTP('tjagksro.cafe24.com','tjagksro','Fitzme123!@')
    # ftp.retrlines('LIST')

    url_list = []
    # for url in range(len(model_img_urls)):
    #     new_id = f"{d['nobg_id']}__{'_'.join(map(str, d['model_ids']))}.jpg"

    # result=TOG.get_tryon(nobg_img_url, model_img_urls[url], part=part)
    # img_result = TryOnImage.objects.create(image=result, title=title)
    # new_url = f'STOR/web/{new_id}'
    # url_list.append(new_url)

    # ftp.storbinary(new_url, result)

    # ftp.quit()

    htmls = make_html(url_list)
    templates = TemplatePage.objects.create(title=title, name='name', part=part,
                                            single_line=htmls[0],
                                            grid=htmls[1],
                                            zigzag=htmls[2]
                                            )

    serializer_class = TemplateSerializer(templates)

    return JsonResponse(serializer_class.data, safe=False)
