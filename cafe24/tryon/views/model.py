import json
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.decorators import api_view, parser_classes
from drf_yasg.utils import swagger_auto_schema

from tryon.serializers import ModelSerializer
from tryon.models import Models


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
    operation_description="Step1. 모델 이미지 등록에 사용될 API",
    request_body=ModelSerializer,
    responses={
        200: ModelSerializer,
        404: "Not Found",
    },
    tags=['Model']
)
@api_view(['GET', 'POST'])
@parser_classes((MultiPartParser, FileUploadParser))
def model_image(request):
    if request.method == 'GET':
        try:
            post = Models.objects.all()
        except Models.DoesNotExist:
            return HttpResponse(status=404)

        serializer = ModelSerializer(post, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(content=json.dumps(serializer.data), status=200)
