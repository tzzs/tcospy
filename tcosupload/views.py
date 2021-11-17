from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm

# Create your views here.


def index(request):
    return HttpResponse("hello world")


def upload(request):
    print(request.FILES.get('file'))
    if request.method == 'POST':
        file = request.FILES.get('file')
        with open(file.name, 'wb') as f:
            f.write(file.read())
            f.close()
        # todo upload files to tencent cos
        msg = 'successful'
    else:
        msg = 'request method error'
    return HttpResponse(msg)
