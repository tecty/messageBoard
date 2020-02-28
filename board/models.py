from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey, DecimalField, CharField, DateTimeField
# Create your models here.


class Message(models.Model):
    issue_user = ForeignKey(
        User, on_delete=models.SET_NULL,
        related_name="%(class)s_issue_user",
        null=True
    )
    title = CharField(max_length=1023)
    body = CharField(max_length=16383)
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)

    reply_body = CharField(max_length=16383, null=True)
    reply_user = ForeignKey(User, on_delete=models.PROTECT, null=True)
    reply_at = DateTimeField(null=True)
