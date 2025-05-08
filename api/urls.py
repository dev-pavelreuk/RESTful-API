from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, CategoryViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
]
