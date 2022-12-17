from django.contrib import admin
from django.urls import path, include
from core.views import handler404, handler403, handler400, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),

    # reference the authentication system
    path('membership/', include('django.contrib.auth.urls')),

    path('membership/', include('membership.urls')),
]

handler400 = handler400
handler404 = handler404
handler403 = handler403
handler500 = handler500

