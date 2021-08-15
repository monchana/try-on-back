from dataclasses import asdict, dataclass
from typing import Dict, List
import base64

import requests
from tryon.exceptions.cafe import CafeTokenNotExistInCache, InvalidToken
from tryon.utils.singleton import SingletonInstance


def _encode_str(string) -> str:
    return base64.b64encode(string.encode('utf-8')).decode('utf-8')


def _get_encoded_auth() -> str:
    return "Basic " + _encode_str(f"{DEVELOPER_CLIENT_ID}:{DEVELOPER_CLIENT_SECRET}")


DEVELOPER_CLIENT_ID = 'f31zyAgabCWXPLDAqtLYdD'
DEVELOPER_CLIENT_SECRET = 'e3F4G6bgACTXhbovBCCMnE'
# CACHE_EXPIRE_TIME = round(60 * 60 * 1.5)
API_URL = 'https://{shop_id}.cafe24api.com'
REDIRECT_URL = "https://pan.snu.ac.kr:8085"
TOKEN_URL = "{api_url}/api/v2/oauth/token"
TOKEN_HEADER = {
    'Authorization': _get_encoded_auth(),
    'Content-Type': 'application/x-www-form-urlencoded',
}
API_VERSION = "2021-06-01"


@dataclass
class Token:
    access_token: str
    expires_at: str  # 2 Hour
    refresh_token: str
    refresh_token_expires_at: str  # 14 Day
    client_id: str
    mall_id: str
    user_id: str
    scopes: List[str]
    issued_at: str


class Cafe(SingletonInstance):
    def __init__(self) -> None:
        self.tokens: Dict[str, Token] = {}

    @staticmethod
    def get_token_url(shop_id: str) -> str:
        base_api_url = API_URL.format(shop_id=shop_id)
        return TOKEN_URL.format(api_url=base_api_url)

    def token_refesh(self, shop_id):
        token = self.tokens.get(shop_id)
        if token is None:
            raise CafeTokenNotExistInCache()
        resp = requests.post(
            url=self.get_token_url(shop_id),
            data={
                "grant_type": "refresh_token",
                "refresh_token": token.refresh_token
            },
            headers=TOKEN_HEADER
        )
        resp.raise_for_status()
        new_token = Token(**resp.json())
        self.tokens[shop_id] = new_token

    def set_token(self, shop_id: str, token):
        if isinstance(token, Token):
            self.tokens[shop_id] = token
        elif isinstance(token, dict):
            self.tokens[shop_id] = Token(**token)
        else:
            raise InvalidToken()

    def get_token(self, code, shop_id) -> Token:
        resp = requests.post(url=self.get_token_url(shop_id), data={
            'grant_type': "authorization_code",
            'code': code,
            'redirect_uri': REDIRECT_URL
        }, headers=TOKEN_HEADER)
        resp.raise_for_status()
        return Token(**resp.json())
