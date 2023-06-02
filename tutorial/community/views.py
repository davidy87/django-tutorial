from django.shortcuts import render
from community.forms import *
from django.http import HttpResponse

from django.views import generic


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def write(request):
    if request.method == 'POST':
        form = Form(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = Form()

    return render(request, 'write.html', {'form': form})

class ListView(generic.ListView):
    model = Article
    template_name = 'list.html'

# def list(request):
#     article_list = Article.objects.all()

#     return render(request, 'list.html', {'article_list': article_list})

class ListView(generic.DetailView):
    model = Article
    template_name = 'list.html'

# def view(request, num="1"):
#     article = Article.objects.get(id=num)

#     return render(request, 'view.html', {'article': article})