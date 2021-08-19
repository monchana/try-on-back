from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from tryon.views import *

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
router = DefaultRouter()
router.register(r'model', TryModelViewSet, basename='models')
urlpatterns = [
    path('product/', product_image),  # step2
    path('gen_tryon_models/', gen_tryon_models),  # step3
    path('register_page/', register_page),  # step4

    # Auth
    path('set_token/', set_token),
    path('refresh_token/', refresh_token),



    # API Document
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0)),
    re_path('swagger.(json|yaml)$', schema_view.without_ui(cache_timeout=0))


    # path('category/<int:numbering>/', views.post_list),
    # path('confirmed/directory/<str:filename>/<str:new_category>/', views.confirm_directory),
] + router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
