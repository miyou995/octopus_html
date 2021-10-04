

from django.contrib import admin
from django.urls import path, include
from config.settings import base
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
]

urlpatterns += static(base.STATIC_URL, document_root=base.STATIC_ROOT)
urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)

if base.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),