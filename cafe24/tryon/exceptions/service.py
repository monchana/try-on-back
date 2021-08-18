from rest_framework.exceptions import APIException


class InvalidSerializerType(APIException):
    status_code = 500
    default_detail = '해당 서비스 로직에서는 사용할 수 없는 Serializer 타입입니다.'
    default_code = 'invalid_serializer_type'
