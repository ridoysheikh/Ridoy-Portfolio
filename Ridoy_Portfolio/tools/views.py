from django.shortcuts import render
from pytube import YouTube
from django.http import HttpResponse

# Create your views here.
def you_tube(request):
    if request.method == "POST":
        try:
            # Enter the YouTube video URL
            video_url=request.POST.get('link')
            print(video_url)
            # Create a YouTube object
            video = YouTube(video_url)
            # Get all available streams
            streams = video.streams.all()
            # Create a list of dictionaries to store the stream information
            stream_info_list = []
            # Loop through each stream and add its information to the list
            for stream in streams:
                stream_info = {
                    "itag": stream.itag,
                    "resolution": f"{stream.resolution}",
                    "size": round(stream.filesize / 1024, 2),  # convert bytes to KB and round to 2 decimal places
                    "type": stream.mime_type.split("/")[-1],
                    }
                stream_info_list.append(stream_info)
            return render(request,'tools/youtube.html',{"link":video_url,"video":stream_info_list})
        except Exception as e:
            
            return render(request,'tools/youtube.html',{"err":str(e)})
    if request.GET.get('url'):
        try:
            format=request.GET.get('format')
            video_url=request.GET.get('url')
            itag = request.GET.get('itag')
            yt = YouTube(video_url)
            # # Get all available streams
            # streams = yt.streams.all()
            stream = yt.streams.get_by_itag(itag)

            response = HttpResponse(content_type='video/mp4')
            response['Content-Disposition'] = f'attachment; filename="{yt.title}.{format}"'
            stream.stream_to_buffer(response)
            return response
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    return render(request,'tools/youtube.html',{})