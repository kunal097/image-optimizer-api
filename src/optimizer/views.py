from django.shortcuts import render
from django.http import JsonResponse
from .models import Image,Temp_User,AuthToken
from.utils import compress , get_client_ip
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required()
def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # print(uploaded_file_url)
        # print(dir(request))
        # print(request.get_host())

        # print('********00')
        # print(fs.location)        Absolute location of uploaded media file

        img = Image()
        img.url = 'http://'+request.get_host()+uploaded_file_url
        img.quality = request.POST['quality']

        # if request.POST['dimension']:
        obj=img.save()

        path = compress(img)

        url = 'http://'+str(request.get_host())+path[path.index('/media'):]


        return render(request, 'optimizer/index.html', {
            'uploaded_file_url': url
        })
    return render(request, 'optimizer/index.html')



@csrf_exempt
def home(request):
    if request.method=='POST':




        # if request.user.is_anonymous:
        #     client_ip = get_client_ip(request)
        #     print('********')
        #     # tu_obj = Temp_User.objects.get(ip_address = str(client_ip))


        #     try:


        #         tu_obj = Temp_User.objects.get(ip_address = str(client_ip))
        #         print('#######')


        #         created_date = str(tu_obj.time_stamp.date())

        #         today = str(datetime.today().date())

        #         if today in created_date:
        #             if tu_obj.count >=5 :


        #                 return JsonResponse({'Message':'Limit exceed. Please Register to get access without limits'})
        #                 # return redirect(RegisterView , permanent=True)

        #             else:
        #                 tu_obj.count +=1
        #                 tu_obj.save()
        #         else:
        #             tu_obj.time_stamp=datetime.today()
        #             tu_obj.count=0
        #             tu_obj.save()

        #     except:
        #         Temp_User.objects.create(ip_address=client_ip)

        api_key = request.POST.get('api')
        try:
            AuthToken.objects.get(api_key=api_key)
        except:
            return JsonResponse({'Response' : 'You are not authorised'})


        img = Image()
        img.url = request.POST['url']
        img.quality = request.POST['quality']
        img.dimension = request.POST.get('dimension')
        # if request.POST['dimension']:
        obj=img.save()

        path = compress(img)

        url = 'http://'+str(request.get_host())+path[path.index('/media'):]







        return JsonResponse({'Response' : url,'Quality':img.quality,'Dimension':img.dimension})


    else:
        return JsonResponse({'Message':'Enjoy Image compression api service'})


