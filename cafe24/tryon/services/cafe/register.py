import requests
from django.db import transaction
from tryon.services.cafe.cafe import Cafe
from tryon.models.models import ProductNB, TemplatePage
from tryon.exceptions.service import InvalidSerializerType
from tryon.services.cafe.tryon_ftp import get_user_info, send_image_ftp


@transaction.atomic
def register_product(serializer):
    if serializer.__class__.__name__ == 'RegisterTemplateSerializer':
        pass
    else:
        raise InvalidSerializerType
    valid_data = serializer.validated_data
    temp = TemplatePage.objects.get(pk=valid_data['template_id'])
    prod = ProductNB.objects.get(pk=valid_data['productnb_id'])
    html = getattr(temp, valid_data['layout'])
    detail_img = prod.image
    user_info = get_user_info()
    cafe = Cafe()
    user = user_info['user']
    tryon_urls = send_image_ftp()
    token = cafe.tokens[user]
    requests.post(
        url=f"{user_info['shop_url']}/api/v2/admin/products",
        data={
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
