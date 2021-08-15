from dataclasses import asdict
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from tryon.services.cafe import Cafe
from tryon.serializers.cafe_auth import ShopIdSerializer, CodeSerializer


@swagger_auto_schema(
    method='post',
    operation_id="Refresh Token of Cafe",
    request_body=ShopIdSerializer,
    operation_description="카페24 Token Refresh",
    responses={
        200: 'Good',
        404: "Not Found",
    },
    tags=['Token']
)
@api_view(['POST'])
def refresh_token(request):
    serializer = ShopIdSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    shop_id = serializer.data['shop_id']
    cafe = Cafe()
    cafe.token_refesh(shop_id)
    return Response(data=cafe.tokens[shop_id], status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='post',
    operation_id="Set Token of Cafe",
    request_body=CodeSerializer,
    operation_description="카페24 Set Token",
    responses={
        200: 'Good',
        404: "Not Found",
    },
    tags=['Token']
)
@api_view(['POST'])
def set_token(request):
    cafe = Cafe()
    serializer = CodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    shop_id = serializer.data['shop_id']
    token = cafe.get_token(code=serializer.data['code'], shop_id=shop_id)
    cafe.set_token(shop_id, token)
    return Response(data=asdict(cafe.tokens[shop_id]), status=status.HTTP_200_OK)
