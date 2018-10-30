from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('groups/', include('groups.urls')),
    path('api_v1/', include('api.urls'))
]
