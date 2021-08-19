from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from tryon.services.cafe.cafe import Cafe

from tryon.models.models import ProductNB, TemplatePage
from tryon.serializers import RegisterTemplateSerializer


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
    serializer = RegisterTemplateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data
    template = TemplatePage.objects.get(pk=data['template_id'])
    html = getattr(template, data['layout'])
    prod = ProductNB.objects.get(pk=data['productnb_id'])
    pub_title = data['title']
    cafe = Cafe()
    result = cafe.register_prod(
        shop_id=data["user_id"],
        json={
            "shop_no": 1,
            "request": {
                "display": "T",
                "selling": "T",
                "description": "<h1> Test </h1> <img src='https://cdn.pixabay.com/photo/2018/05/17/06/22/dog-3407906_960_720.jpg' />",
                "detail_image": "/web/product/medium/202108/22585dfd9401361d03d7449ec1056f36.png",
                "add_category_no": [
                    {
                        "category_no": 43,
                        "recommend": "F",
                        "new": "T"
                    }
                ],
                "product_name": "asd",
                "supply_price": 4000,
                "price": 12300
            }
        }
    )
    if result is True:
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
