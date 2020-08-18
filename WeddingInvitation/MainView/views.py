from django.shortcuts import render
from django.views.generic import TemplateView

from MainView.forms import InvitationForm
from MainView.models import ConfirmAnswer

class InvitationView(TemplateView):

    template_name = 'home/invitation.html'

    def get(self, request):

        form = InvitationForm()

        args = { 'form': form }

        return render(request, self.template_name, args)

    def post(self, request):

        form = InvitationForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user

            if ConfirmAnswer.objects.filter(user=post.user).exists():
                if not ConfirmAnswer.objects.get(user = post.user, answer_sent = True):
                    post.save()
            else:
                post.save()

            text = form.cleaned_data['answer_sent']

        args = { 'form': form, 'text': text}

        return render(request, self.template_name, args)

def index(request):

    template_name = 'home/index.html'

    return render(request, template_name)
