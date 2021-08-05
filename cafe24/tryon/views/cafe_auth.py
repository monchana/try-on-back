import base64
from django.http import response
from rest_framework import status
import requests
from typing import List, Final
from dataclasses import dataclass
from rest_framework.decorators import api_view

from tryon.exceptions.cafe import CafeTokenNotExistInCache


class Token(dataclass):
    access_token: str
    expires_at: str  # 2 Hour
    refresh_token: str
    refresh_token_expires_at: str  # 14 Day
    client_id: str
    mall_id: str
    user_id: str
    scopes: List[str]
    issued_at: str


def get_token_url(shop_id: str) -> str:
    base_api_url = API_URL.format(shop_id=shop_id)
    return TOKEN_URL.format(api_url=base_api_url)


def encode_str(string) -> str:
    return base64.b64encode(string.encode('utf-8')).decode('utf-8')


def get_encoded_auth() -> str:
    return "Basic " + encode_str(f"{DEVELOPER_CLIENT_ID}:{DEVELOPER_CLIENT_SECRET}")


DEVELOPER_CLIENT_ID: Final[str] = 'f31zyAgabCWXPLDAqtLYdD'
DEVELOPER_CLIENT_SECRET: Final[str] = '29eBoMseokKvOAlh1jWqQM'
CACHE_EXPIRE_TIME: Final[int] = round(60 * 60 * 1.5)
API_URL = 'https://{shop_id}.cafe24api.com'
TOKEN_URL = "{api_url}/api/v2/oauth/token"
TOKEN_HEADER = {
    'Authorization': get_encoded_auth(),
    'Content-Type': 'application/x-www-form-urlencoded',
},


@api_view(['POST'])
def refresh_token(request):
    data = {
        "grant_type": "refresh_token",
        "refresh_token": request.data.get('refresh_token')
    }
    resp = requests.post(
        url=get_token_url(request.data.get('shop_id')),
        data=data,
        headers=TOKEN_HEADER
    )
    cafe = Token(**resp.json())
    resp.raise_for_status()
    return response(data=cafe._asdict(), status=status.HTTP_200_OK)


@api_view(['POST'])
def set_token_from_cafe(request):
    resp = requests.post(
        url=get_token_url(request.data.get("shop_id")),
        data={
            'grant_type': 'authorization_code',
            'code': request.data.get("code"),
            'redirect_uri': 'https://try-on.netlify.app'
        }, headers=TOKEN_HEADER
    )
    resp.raise_for_status()
    return Token(**resp.json())
