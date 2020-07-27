from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from manager.views import home

urlpatterns = [
    path("", home.index, name="home"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns