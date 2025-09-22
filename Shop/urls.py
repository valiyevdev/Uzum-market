from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # Bu yerni to‘g‘riladik — 'set_language' ni to‘g‘ri joyga qo‘ydik
    path('i18n/', include('django.conf.urls.i18n')),
]

# i18n_patterns — tilga bog‘liq marshrutlar shu yerda
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    path('auth/', include('Authentication.urls')),
    path('', include('Admin.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


