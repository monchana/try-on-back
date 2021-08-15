from rest_framework import serializers


class ShopIdSerializer(serializers.Serializer):
    shop_id = serializers.CharField()


class CodeSerializer(ShopIdSerializer):
    code = serializers.CharField()
