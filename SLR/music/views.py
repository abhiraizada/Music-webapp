#2from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Album,Song
def index(request):
    all_albums = Album.objects.all()
    #1template= loader.get_template('music/index.html')
    context ={
        'all_albums': all_albums,
    }

    #1return HttpResponse(template.render(context,request))
    return render(request,'music/index.html',context)
def detail(request,music_id):
    #1return HttpResponse("<h1> Welcome in id:"+str(music_id)+"</h1>")
    #2try:
        #2m1=Album.objects.get(pk=music_id)
    #2except Album.DoesNotExist:
        #2raise Http404("BC Spotify nai hai jo har gaana milega")
    m1=get_object_or_404(Album,pk=music_id)
    return render(request,'music/index.html',{'m1':m1})
def favorite(request, music_id):
    m1=get_object_or_404(Album,pk=music_id)
    try:
        selected_song=m1.song_set.get(pk=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render( request,'music/index1.html',{'m1':m1,'error_message':"you did not select song"})
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render( request,'music/index1.html',{'m1':m1})
