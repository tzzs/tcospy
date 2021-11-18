from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
import time
from tcosupload.service import *
from tcospy.Msg import *
import json

# Create your views here.


def index(request):
    return HttpResponse("hello world")


def upload(request):
    # upload files to tencent cos

    msg = Msg()
    msg.code = 200

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
        url = uploadFiles(file_path)
        msg.msg = 'successful'
        msg.data = {'url': url, 'name': file.name}
    else:
        msg.code = 410
        msg.msg = 'request method error'
    return HttpResponse(json.dumps(msg.__dict__))
