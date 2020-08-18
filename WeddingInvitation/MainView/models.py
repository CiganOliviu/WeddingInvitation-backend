from django.db import models
from django.contrib.auth.models import User

class ConfirmAnswer (models.Model):
    answer_sent = models.BooleanField(default = False)
    submitted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
