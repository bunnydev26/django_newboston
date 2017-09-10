from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Album, Song


# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = { 'all_albums': all_albums, }
    # return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    # try:
    #     album = Album.objects.get(id=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album doesnot exists")

    album = get_object_or_404(Album, id=album_id)

    return render(request, 'music/detail.html', {'album' : album})
