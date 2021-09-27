from rest_framework import authentication
from chat.models import (
    MessageAction,
    ThreadMember,
    Thread,
    Message,
    ThreadAction,
    ForwardedMessage,
)
from .serializers import (
    MessageActionSerializer,
    ThreadMemberSerializer,
    ThreadSerializer,
    MessageSerializer,
    ThreadActionSerializer,
    ForwardedMessageSerializer,
)
from rest_framework import viewsets


class ThreadActionViewSet(viewsets.ModelViewSet):
    serializer_class = ThreadActionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ThreadAction.objects.all()


class ForwardedMessageViewSet(viewsets.ModelViewSet):
    serializer_class = ForwardedMessageSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ForwardedMessage.objects.all()


class ThreadMemberViewSet(viewsets.ModelViewSet):
    serializer_class = ThreadMemberSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ThreadMember.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Message.objects.all()


class MessageActionViewSet(viewsets.ModelViewSet):
    serializer_class = MessageActionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = MessageAction.objects.all()


class ThreadViewSet(viewsets.ModelViewSet):
    serializer_class = ThreadSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Thread.objects.all()
