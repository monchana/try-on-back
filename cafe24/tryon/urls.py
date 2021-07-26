from django.urls import path
from django.views.generic import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from tryon.views import model_image

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('model/', model_image.model_image),
    path('product/', model_image.product_image),

    path('detail/', views.detail_page),
    path('create_template/', views.create_template),
    path('layout_page/', views.layout_page),

    path('register_page/', views.register_page),

    # path('category/<int:numbering>/', views.post_list),
    # path('confirmed/directory/<str:filename>/<str:new_category>/', views.confirm_directory),
]