from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # include our custom app urls here
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)