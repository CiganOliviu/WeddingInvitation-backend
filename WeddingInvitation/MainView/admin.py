from django.contrib import admin
from .models import ConfirmAnswer

class ConfirmAnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'answer_sent')

admin.site.register(ConfirmAnswer, ConfirmAnswerAdmin)
