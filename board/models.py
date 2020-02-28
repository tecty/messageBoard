from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey, DecimalField, CharField, DateTimeField, OneToOneField
# Create your models here.


class Reply(models.Model):
    reply_body = CharField(max_length=16383)
    reply_user = ForeignKey(User, on_delete=models.PROTECT)
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)


class Message(models.Model):
    issue_user = ForeignKey(User, models.SET_NULL, null=True)
    title = CharField(max_length=1023)
    body = CharField(max_length=16383)
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)
    reply = OneToOneField(Reply, models.SET_NULL, null=True)
