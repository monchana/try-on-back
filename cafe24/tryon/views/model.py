import json
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.decorators import api_view, parser_classes
from drf_yasg.utils import swagger_auto_schema

from tryon.serializers import ModelSerializer
from tryon.models import Models


@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_id="모델 생성",
    operation_description="모델을 생성합니다.",
    tags=['Model'],
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_id="단일 모델 얻어오기",
    operation_description="단일 모델 정보를 제공합니다",
    tags=['Model'],
))
@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_id="모델 정보 리스트",
    operation_description="모델 목록을 받아옵니다",
    tags=['Model'],
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_id="모델 정보 부분 변경",
    operation_description="모델 정보 부분변경 기능을 제공 합니다.",
    tags=['Model'],
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_id="모델 정보 변경",
    operation_description="모델 정보를 변경 기능을 제공 합니다.",
    tags=['Model'],
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_id="모델 삭제",
    operation_description=" 특정 ID의 모델를 삭제 기능을 제공합니다.",
    tags=['Model'],
))
class TryModelViewSet(viewsets.ModelViewSet):
    queryset = Models.objects.all()
    parser_classes = (MultiPartParser, FileUploadParser)
    serializer_class = ModelSerializer
