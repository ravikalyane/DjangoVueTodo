from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('TodoApi', views.TodoView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name="home")
]
