from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    MessageActionViewSet,
    ThreadMemberViewSet,
    ThreadViewSet,
    MessageViewSet,
    ThreadActionViewSet,
    ForwardedMessageViewSet,
)

router = DefaultRouter()
router.register("threadaction", ThreadActionViewSet)
router.register("forwardedmessage", ForwardedMessageViewSet)
router.register("threadmember", ThreadMemberViewSet)
router.register("message", MessageViewSet)
router.register("messageaction", MessageActionViewSet)
router.register("thread", ThreadViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
