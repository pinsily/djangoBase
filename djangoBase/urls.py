from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userprofile.urls')),
    path('', include('front.urls')),
    path('accounts/', include('allauth.urls')),
    # re_path('media/?P<path>.*', serve, {'document_root': settings.MEDIA_ROOT}, name="media")
]


