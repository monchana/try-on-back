from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from tryon.models import Models, Product, ProductNB, TemplatePage, TryOnImage

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models
        fields = ('id', 'image',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'image', 'part')


class ProductNBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductNB
        fields = ('id', 'title', 'image', 'part', 'product')

class TemplatePostSerializer(serializers.Serializer):
    model_ids = serializers.ListField(
        child=serializers.IntegerField())
    nobg_id = serializers.IntegerField()

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplatePage
        fields = ('id', 'name', 'title', 'part', 'single_line', 'grid', 'zigzag')


class TryOnImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TryOnImage
        fields = ('id', 'name', 'template', 'image', 'default')

class RegisterTemplateSerializer(serializers.Serializer):
    template_id = serializers.IntegerField()

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]