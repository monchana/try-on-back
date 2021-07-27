from django.urls import path, re_path
from django.views.generic import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from tryon.views.model_image import *

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
    path('model/', model_image),
    path('product/', product_image),

    path('detail/', detail_page),
    path('create_template/', create_template),
    path('layout_page/', layout_page),

    path('register_page/', register_page),

   # API Document
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0)),
    re_path('swagger.(json|yaml)$', schema_view.without_ui(cache_timeout=0))


    # path('category/<int:numbering>/', views.post_list),
    # path('confirmed/directory/<str:filename>/<str:new_category>/', views.confirm_directory),
]