from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from tryon.models import Models, Product, ProductNB, TemplatePage, TryOnImage

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('image', 'part')


class ProductNBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductNB
        fields = ('title', 'image')


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplatePage
        fields = ('name', 'title', 'part', 'single_line', 'grid', 'zigzag')


class TryOnImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TryOnImage
        fields = ('name', 'template', 'image', 'default')

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