from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProfileViewSet, VerificationCodeViewSet, ContactViewSet

router = DefaultRouter()
router.register("verificationcode", VerificationCodeViewSet)
router.register("profile", ProfileViewSet)
router.register("contact", ContactViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
