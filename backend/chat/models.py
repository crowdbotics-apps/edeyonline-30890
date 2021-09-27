from django.conf import settings
from django.db import models


class ThreadAction(models.Model):
    "Generated Model"
    action = models.CharField(
        max_length=7,
    )
    thread = models.ForeignKey(
        "chat.Thread",
        on_delete=models.CASCADE,
        related_name="threadaction_thread",
    )
    profile = models.ForeignKey(
        "chat_user_profile.Profile",
        on_delete=models.CASCADE,
        related_name="threadaction_profile",
    )
    timestamp_action = models.DateTimeField(
        auto_now_add=True,
    )


class ForwardedMessage(models.Model):
    "Generated Model"
    message = models.ForeignKey(
        "chat.Message",
        on_delete=models.CASCADE,
        related_name="forwardedmessage_message",
    )
    forwarded_by = models.ForeignKey(
        "chat_user_profile.Profile",
        on_delete=models.CASCADE,
        related_name="forwardedmessage_forwarded_by",
    )
    forwarded_to = models.ForeignKey(
        "chat.Thread",
        on_delete=models.CASCADE,
        related_name="forwardedmessage_forwarded_to",
    )
    timestamp_forwarded = models.DateTimeField(
        auto_now_add=True,
    )


class ThreadMember(models.Model):
    "Generated Model"
    profile = models.ForeignKey(
        "chat_user_profile.Profile",
        on_delete=models.CASCADE,
        related_name="threadmember_profile",
    )
    thread = models.ForeignKey(
        "chat.Thread",
        on_delete=models.CASCADE,
        related_name="threadmember_thread",
    )
    is_admin = models.BooleanField()
    timestamp_joined = models.DateTimeField(
        auto_now_add=True,
    )
    timestamp_left = models.DateTimeField()
    last_rejoined = models.DateTimeField()


class Message(models.Model):
    "Generated Model"
    message = models.TextField()
    thread = models.ForeignKey(
        "chat.Thread",
        on_delete=models.CASCADE,
        related_name="message_thread",
    )
    sent_by = models.ForeignKey(
        "chat.ThreadMember",
        on_delete=models.CASCADE,
        related_name="message_sent_by",
    )
    attachment = models.URLField()
    is_draft = models.BooleanField()
    is_delivered = models.BooleanField()
    is_read = models.BooleanField()
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )
    timestamp_delivered = models.DateTimeField()
    timestamp_read = models.DateTimeField()


class MessageAction(models.Model):
    "Generated Model"
    action = models.CharField(
        max_length=7,
    )
    message = models.ForeignKey(
        "chat.Message",
        on_delete=models.CASCADE,
        related_name="messageaction_message",
    )
    profile = models.ForeignKey(
        "chat_user_profile.Profile",
        on_delete=models.CASCADE,
        related_name="messageaction_profile",
    )
    timestamp_action = models.DateTimeField(
        auto_now_add=True,
    )


class Thread(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=255,
    )
    thread_photo = models.URLField()
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )


# Create your models here.
