from django.conf import settings
from django.db import models


class VerificationCode(models.Model):
    "Generated Model"
    code = models.CharField(
        max_length=255,
    )
    sent_to = models.ForeignKey(
        "chat_user_profile.Profile",
        on_delete=models.CASCADE,
        related_name="verificationcode_sent_to",
    )
    is_verified = models.BooleanField()
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )
    timestamp_verified = models.DateTimeField()


class Profile(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="profile_user",
    )
    mobile_number = models.CharField(
        max_length=20,
    )
    pin = models.CharField(
        max_length=100,
    )
    photo = models.URLField()
    status = models.CharField(
        max_length=50,
    )
    birthdate = models.DateField()
    gender = models.CharField(
        max_length=1,
    )
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated = models.DateTimeField(
        auto_now=True,
    )
    last_login = models.DateTimeField()


class Contact(models.Model):
    "Generated Model"
    added_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="contact_added_by",
    )
    added_profile = models.ForeignKey(
        "chat_user_profile.Profile",
        on_delete=models.CASCADE,
        related_name="contact_added_profile",
    )
    is_blocked = models.BooleanField()
    is_favorite = models.BooleanField()
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )


# Create your models here.
