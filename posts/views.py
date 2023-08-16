from django.shortcuts import render

from posts import models


# Create your views here.
def home(request):
    return render(request, 'posts/index.html', {'post': models.chat.objects.all()})