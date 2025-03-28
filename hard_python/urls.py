
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('main/', include('main_app.urls'))
]
