from tryon.models.models import TryOnImage
from django.http import JsonResponse
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from django.core.files import File
from urllib import request as req

from tryon.serializers import TemplatePostSerializer, CreateTemplateSerializer
from tryon.models import Models, ProductNB, TemplatePage
from tryon.services.cafe.tryon_ftp import send_image_ftp, get_user_info


@swagger_auto_schema(
    method='post',
    operation_id="Template Post",
    operation_description="Step3. 상세 페이지 생성에서 사용되는 API",
    request_body=TemplatePostSerializer,
    responses={
        200: CreateTemplateSerializer,
        404: "Not Found",
    },
    tags=['Template']
)
@api_view(['POST'])
def create_template(request):
    serializer = TemplatePostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    d = serializer.validated_data

    nobg_post = ProductNB.objects.get(id=d['nobg_id'])
    model_imgs_path = [
        p.image.path for p in Models.objects.filter(id__in=d['model_ids'])]
    nobg_img_path = nobg_post.image.path

    imgdict_list = generate_tryon(
        prodnb_img_path=nobg_img_path, model_imgs_path=model_imgs_path)
    htmls = make_html('')
    tryons = []
    for d in imgdict_list:
        if 'model' in d['src']:
            tryons.append(TryOnImage(name="", image=File(
                open(d['src'], 'rb')), default=False))
    tryon_imgs = TryOnImage.objects.bulk_create(tryons)
    template = TemplatePage.objects.create(
        title=nobg_post.title, name='name', part=nobg_post.part, **htmls)
    serializer = CreateTemplateSerializer(
        {"template": template, "tryon_imgs": tryon_imgs})
    return JsonResponse(serializer.data, safe=False)

# Temp =====


def make_html(images):
    return {
        "single_line": "<h1> Single line </ h1>",
        "grid": "<h2> Grid </ h2>",
        "zigzag": "<h3> ZigZag </ h3>",
    }


def generate_tryon(prodnb_img_path, model_imgs_path):
    imgdict_list = []
    for i in model_imgs_path:
        imgdict_list.append({"src": i, "dest": f'models/{i.split("/")[-1]}'})
    imgdict_list.append(
        {"src": prodnb_img_path, "dest": f'products/{prodnb_img_path.split("/")[-1]}'})
    send_image_ftp(imgdict_list, **get_user_info())
    return imgdict_list

# ===== Temp
