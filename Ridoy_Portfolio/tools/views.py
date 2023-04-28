from django.shortcuts import render
import requests
from pytube import YouTube
from django.http import HttpResponse, StreamingHttpResponse
import youtube_dl

# Create your views here.
def you_tube(request):
    if request.method == "POST":
        try:
            # video_url=request.POST.get('link')
            # video = YouTube(video_url)
            # streams = video.streams.all()
            # stream_info_list = []
            # for stream in streams:
            #     stream_info = {
            #         "itag": stream.itag,
            #         "resolution": f"{stream.resolution}",
            #         "size": round(stream.filesize / 1024, 2),
            #         "type": stream.mime_type.split("/")[-1],
            #         }
            #     stream_info_list.append(stream_info)
            # return render(request,'tools/youtube.html',{"link":video_url,"video":stream_info_list})
            video_url = request.POST.get('link')
            ydl_opts = {
                'format': 'best',
                'quiet': True,
                'no_warnings': True,
                'forcejson': True,
                'simulate': True,
                'youtube_include_dash_manifest': False
                }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                video_info = ydl.extract_info(video_url, download=False)
                stream_info_list = []
                for stream in video_info['formats']:
                    stream_info = {
                        "itag": stream['format_id'],
                        "resolution": stream.get('height', 'audio only'),
                        "size": f"{round(int(stream.get('filesize', -1))/(1024*1024), 2)} MB" if stream.get('filesize') is not None else "Unknown",
                        "type": stream['ext'],
                        "url": stream['url']
                        }
                    stream_info_list.append(stream_info)
            return render(request, 'tools/youtube.html', {"link": video_url, "video": stream_info_list})
        except Exception as e:
            return render(request,'tools/youtube.html',{"err":str(e)})
    if request.GET.get('url'):
        try:
            format = request.GET.get('format')
            video_url = request.GET.get('url')
            itag = request.GET.get('itag')
            heit = request.GET.get('height')


            ydl_opts = {
                'format': f'bestvideo[height={heit}]+bestaudio/best[height={heit}]',
                'outtmpl': '%(title)s.%(ext)s',
                'quiet': True,
            }

            ydl = youtube_dl.YoutubeDL(ydl_opts)
            info_dict = ydl.extract_info(video_url, download=False)
            video_url = info_dict['formats'][0]['url']

            headers = {
                'Accept-Encoding': 'identity',
            }

            response = StreamingHttpResponse(
                requests.get(video_url, headers=headers, stream=True),
                content_type=f'video/{format}',
            )
            response['Content-Disposition'] = f'attachment; filename="{info_dict["title"]}.{format}"'

            return response

        except Exception as e:
            return HttpResponse(f"Error: {e}")
    return render(request,'tools/youtube.html',{})