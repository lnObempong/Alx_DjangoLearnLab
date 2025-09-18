from rest_framework import routers
from django.urls import path, include
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r"books", BookViewSet, basename="book")

urlpatterns = [
    path("", include(router.urls)),
]
