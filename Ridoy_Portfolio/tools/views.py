from django.shortcuts import render
import requests
from django.http import HttpResponse, StreamingHttpResponse, FileResponse
import youtube_dl
import re,sys ,os, io
from io import BytesIO
from pdf2image import convert_from_bytes
import zipfile


# Create your views here.
def you_tube(request):
    if request.method == "POST":
        try:
            video_url = request.POST.get('link')
            ydl_opts = {
                'quiet': True,
                'nocheckcertificate': True,
                'no_call_home': True,
                'verbose': True,
                'no_color': True,
                'no_warnings': True,
                'outtmpl': '%(title)s.%(ext)s',
                'format': 'bestvideo+bestaudio/best',
                'extractor_args': {
                    'youtube': {
                        'skip_unavailable_fragments': True,
                        'ignoreerrors': True,
                        'verbose': True,
                        'no_color': True,
                        'no_warnings': True,
                        'logger': None,
                        'progress_hooks': None,
                        'extract_flat': True,
                    }
                }
            }

            ydl= youtube_dl.YoutubeDL(ydl_opts)
            video_info = ydl.extract_info(video_url, download=False)
            
            # Get Different Sites Vidoes Informations
            if re.match(r"https?://www\.facebook\.com/", video_url):
                video_info=video_info['entries'][0]['formats']

            else:
                video_info=video_info['formats']


            stream_info_list = []
            for stream in video_info:
                if stream['protocol'] == 'https':
                    stream_info = {
                        "itag": stream['format'],
                        "resolution": stream.get('height', 'audio only'),
                        "size": f"{round(int(stream.get('filesize', -1))/(1024), 2)}" if stream.get('filesize') is not None else "Unknown",
                        "type": stream['ext'],
                        "url": stream['url']
                        }
                    stream_info_list.append(stream_info)
                
            return render(request, 'tools/youtube.html', {"link": video_url, "video": stream_info_list})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            e=f'{exc_type}, {fname}, {exc_tb.tb_lineno}'
            return render(request,'tools/youtube.html',{"err":str(e)})
    if request.GET.get('url'):
        try:
            format = request.GET.get('format')
            video_url = request.GET.get('url')
            itag = request.GET.get('itag')
            heit = request.GET.get('height')

            ydl_opts = {
                'quiet': True,
                'nocheckcertificate': True,
                'no_call_home': True,
                'verbose': True,
                'no_color': True,
                'no_warnings': True,
                'outtmpl': '%(title)s.%(ext)s',
                'format': 'bestvideo+bestaudio/best',
                'extractor_args': {
                    'youtube': {
                        'skip_unavailable_fragments': True,
                        'ignoreerrors': True,
                        'verbose': True,
                        'no_color': True,
                        'no_warnings': True,
                        'logger': None,
                        'progress_hooks': None,
                        'extract_flat': True,
                    }
                }
            }

            ydl = youtube_dl.YoutubeDL(ydl_opts)
            info_dict = ydl.extract_info(video_url, download=False)

            # Get Different Sites Vidoes Informations
            if re.match(r"https?://www\.facebook\.com/", video_url):
                video_url = info_dict['entries'][0]['formats']
                for vdo in video_url:
                    if vdo['format'] == itag:
                        video_url = vdo['url']
                    fname=f"fb-video{vdo['format']}"
            else:
                video_url = info_dict['formats']
                for vdo in video_url:
                    if vdo['format'] == itag:
                        video_url = vdo['url']
                fname=info_dict["title"]

            
            headers = {
                'Accept-Encoding': 'identity',
            }

            response = StreamingHttpResponse(
                requests.get(video_url, headers=headers, stream=True),
                content_type=f'video/{format}',
                )
            response['Content-Disposition'] = f'attachment; filename="{fname}.{format}"'

            return response

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            e=f'{exc_type}, {fname}, {exc_tb.tb_lineno}'
            return HttpResponse(f"Error: {e}")
    return render(request,'tools/youtube.html',{})
def pdf_tool(request):
    if request.method == "POST":
        file = request.FILES['file']
        try:
            if file:
                # Read the uploaded PDF file
                pdf_file = file.read()
                # Convert the PDF to a list of PNG images
                images = convert_from_bytes(pdf_file)
                
                # Create a temporary file to hold the ZIP archive
                zip_file = zipfile.ZipFile('temp.zip', 'w')
                
                # Add each image to the ZIP archive
                for i, image in enumerate(images):
                    # Save the PNG image to an in-memory buffer
                    buffer = BytesIO()
                    image.save(buffer, format='PNG')
                    
                    # Add the image to the ZIP archive with a unique filename
                    filename = f'page_{i+1}.png'
                    zip_file.writestr(filename, buffer.getvalue())
                
                # Close the ZIP archive
                zip_file.close()
                
                # Create a response object with the ZIP archive as the content
                response = HttpResponse(open('temp.zip', 'rb'), content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename="output.zip"'
                
                # Delete the temporary file
                os.remove('temp.zip')
                
                # Return the response
                return response
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            e=f'{exc_type}, {fname}, {exc_tb.tb_lineno}'
            return render(request,'tools/pdf.html',{"err":str(e)})
    return render(request,'tools/pdf.html',{})