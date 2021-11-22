from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    # path("", include("core.urls", namespace="core")),
    path("users/", include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root)