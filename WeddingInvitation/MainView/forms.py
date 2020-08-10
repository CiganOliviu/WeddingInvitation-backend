from django import forms
from MainView.models import ConfirmAnswer

class IndexForm(forms.ModelForm):
    answer_sent = forms.BooleanField()

    class Meta:
        model = ConfirmAnswer
        fields = ('answer_sent',)
