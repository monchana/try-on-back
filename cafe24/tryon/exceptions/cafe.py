from rest_framework.exceptions import APIException


class RequireCafeAuthCode(APIException):
    status_code = 400
    default_detail = 'Cafe 24 Authentication Code is not exist in Parameter'
    default_code = 'cafe24_auth_code_is_required'


class CafeTokenNotExistInCache(APIException):
    status_code = 400
    default_detail = 'cafe24_token_not_exist_in_tokens'
    default_code = 'cafe24_token_not_exist_in_tokens'


class InvalidToken(APIException):
    status_code = 400
    default_detail = 'InvalidToken'
    default_code = 'invalid_token'
