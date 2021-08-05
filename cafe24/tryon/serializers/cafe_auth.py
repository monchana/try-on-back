from rest_framework import serializers


class _CommonSerializer(serializers.Serializer):
    shop_id = serializers.CharField()
