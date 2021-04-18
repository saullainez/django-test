from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    path(r'account/', include('account.urls')),
    path('api/', include(router.urls)),
]
