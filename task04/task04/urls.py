from django.contrib import admin
from django.urls import include, path

from . import views


handler404 = views.page_not_found
handler500 = views.error_server
handler403 = views.permission_denied

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usermanager.urls', namespace='manager')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/', views.sign_up, name='registration'),
]
