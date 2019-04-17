from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Post

#def index(request):
#    return HttpResponse("Это тушка нашего сайта.")

def index(request):
    template = loader.get_template('body/index.html')
    posts = Post.objects.order_by('-published')
    context = {'posts' : posts}
    return HttpResponse(template.render(context, request))



