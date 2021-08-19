from django.conf import settings


def get_static_img_path(img_path):
    return img_path.replace(settings.MEDIA_ROOT, '/')
