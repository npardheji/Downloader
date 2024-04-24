from django.shortcuts import render,redirect
from pytube import YouTube 


# Create your views here.
def home(request):
    return render(request,'home.html')



def new_home(request):
    if request.method == 'POST':
        youtube_url = request.POST['mainurl']
        yt = YouTube(youtube_url)
        videos = []
        for stream in yt.streams.filter(progressive=True):
            resolution = stream.resolution
            size_in_mb = round(stream.filesize / (1024 * 1024), 2)
            download_link = stream.url
            title=yt.title
            thumbnail_url = yt.thumbnail_url
            print(">>>>>>>>>>>>>",title)
            videos.append({
                'resolution': resolution,
                'size_in_mb': size_in_mb,
                'download_link': download_link,
                
                
            })
        return render(request, 'yt-home.html', {'videos': videos,'thumbnail_url':thumbnail_url,'title':title,})
    return render(request, 'yt-home.html')