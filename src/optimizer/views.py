from django.shortcuts import render
from django.http import JsonResponse
from .models import Image,Temp_User
from.utils import compress , get_client_ip
from datetime import datetime

# Create your views here.
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    if request.method=='POST':



        if request.user.is_anonymous:
            client_ip = get_client_ip(request)
            print('********')
            # tu_obj = Temp_User.objects.get(ip_address = str(client_ip))


            try:


                tu_obj = Temp_User.objects.get(ip_address = str(client_ip))
                print('#######')


                created_date = str(tu_obj.time_stamp.date())

                today = str(datetime.today().date())

                if today in created_date:
                    if tu_obj.count >=5 :


                        return JsonResponse({'Message':'Limit exceed. Please Register to get access without limits'})
                        # return redirect(RegisterView , permanent=True)

                    else:
                        tu_obj.count +=1
                        tu_obj.save()
                else:
                    tu_obj.time_stamp=datetime.today()
                    tu_obj.count=0
                    tu_obj.save()

            except:
                Temp_User.objects.create(ip_address=client_ip)


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


