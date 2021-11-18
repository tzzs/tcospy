from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
import time
from tcosupload.service import *

# Create your views here.


def index(request):
    return HttpResponse("hello world")


def upload(request):
    # upload files to tencent cos
    print(request.FILES.get('file'))
    if request.method == 'POST':
        file = request.FILES.get('file')
        file_path = 'files/' + str(int(time.time())) + '-' + file.name

        # save file to local
        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
            f.close()

        # upload files to tencent cos
        uploadFiles(file_path)
        msg = 'successful'
    else:
        msg = 'request method error'
    return HttpResponse(msg)
