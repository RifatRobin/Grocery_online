from django.contrib import admin
from django.urls import path, include

# to have the configuration of the media file we created in BASE_DIR of MEDIA_ROOT in the settings.py
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# for showing the media document like images in the browser when we click in the particular image
