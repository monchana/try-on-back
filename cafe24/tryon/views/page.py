from django.http import HttpResponse
from rest_framework.decorators import api_view
from tryon.serializers import RegisterTemplateSerializer
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='post',
    operation_id="Page Generation Post",
    operation_description="Step4. 레이아웃 선택 / 상품등록 페이지에서 가등록에 사용될 API",
    request_body=RegisterTemplateSerializer,
    responses={
        200: "Good",
        404: "Not Found",
    },
    tags=['Register']
)
@api_view(['POST'])
def register_page(request):
    try:
        serializer = RegisterTemplateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=404)
