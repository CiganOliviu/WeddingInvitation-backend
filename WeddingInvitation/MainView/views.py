from django.shortcuts import render
from django.views.generic import TemplateView

from MainView.forms import IndexForm

class IndexView(TemplateView):

    template_name = 'home/index.html'

    def get(self, request):

        form = IndexForm()

        args = { 'form': form }

        return render(request, self.template_name, args)

    def post(self, request):

        form = IndexForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            text = form.cleaned_data['answer_sent']

        args = { 'form': form, 'text': text}

        return render(request, self.template_name, args)
