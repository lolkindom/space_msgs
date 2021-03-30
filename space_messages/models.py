import datetime

from django.db import models
from json import JSONEncoder


class SpaceMessage(models.Model):
    msg_date = models.DateTimeField()
    text = models.TextField()
    is_read = models.BooleanField()

