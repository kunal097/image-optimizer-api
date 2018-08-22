from django.shortcuts import render
from django.http import JsonResponse
from .models import Image
from.utils import compress

# Create your views here.
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    if request.method=='POST':
        img = Image()
        img.url = request.POST['url']
        img.quality = request.POST['quality']
        img.dimension = request.POST.get('dimension')
        # if request.POST['dimension']:
        obj=img.save()

        path = compress(img)

        url = 'http://'+str(request.get_host())+path[path.index('/media'):]



    return JsonResponse({'Response' : url,'Quality':img.quality,'Dimension':img.dimension})


