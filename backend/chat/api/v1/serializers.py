from rest_framework import serializers
from chat.models import (
    MessageAction,
    ThreadMember,
    Thread,
    Message,
    ThreadAction,
    ForwardedMessage,
)


class ThreadActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadAction
        fields = "__all__"


class ForwardedMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForwardedMessage
        fields = "__all__"


class ThreadMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadMember
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class MessageActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageAction
        fields = "__all__"


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = "__all__"
