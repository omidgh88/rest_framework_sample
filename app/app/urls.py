from django.contrib import admin
from django.urls import path, include
from .api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    # curl -X GET http://127.0.0.1:9999/api/v1/friends/
    path('api/v1/', include(router.urls)),
    # curl -X POST -d '{"username":"omid", "password":"123"}' -H 'Content-Type: application/json' http://localhost:9999/api/auth/token/login
    # curl -X GET http://127.0.0.1:9999/api/v1/friends/ -H 'Authorization: Token 3778c49dae4d8e1f6c4bd6805d43745744608591'
    path('api/auth/', include('djoser.urls.authtoken')),
]
