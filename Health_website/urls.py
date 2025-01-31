from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from image_process.views import upload_image, Home, Acne, hyperpigmentation, Nail_p, Sjs, Vitiligo, Affect
from Cost_calculator.views import user_profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='Home'),
    path('upload/', upload_image, name='upload_image'),
    path('Acne/', Acne, name='Acne'),
    path('hyperpigmentation/', hyperpigmentation, name='hyperpigmentation'),
    path('Nail_p/', Nail_p, name='Nail_p'),
    path('Sjs/', Sjs, name='Sjs'),
    path('Vitiligo/', Vitiligo, name='Vitiligo'),
    path('Affect/', Affect, name='Affect'),


    path('user_profile/', user_profile_view, name='user_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
