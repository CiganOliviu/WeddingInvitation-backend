from django.db import models

class ConfirmAnswer (models.Model):

    name = models.CharField(max_length=200, unique=True)
    submitted = models.BooleanField(default = True)
    answer_sent = models.DateTimeField(auto_now_add=True)
