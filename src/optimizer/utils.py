import os
from PIL import Image


def compress(image):


    img = Image.open(image.local_path)

    if 'png' in image.local_path:
        img = img.convert('P' , palette=Image.ADAPTIVE)

    if  image.dimension:


        width = int(image.dimension)
        # print(type(width))
        height = int((img.size[1]*width)/img.size[0])
        img = img.resize((width,height),Image.ANTIALIAS)

        # path = image.local_path.split('/')
        # print('*********************')
        # print(path)
        # # path = path[path.index('upload')]='output'
        # pos = path.index('upload')
        # path[pos]='output'
        # # print()
        # print('###########3')
        # print(path)
        # path = '/'.join(path)
    if 'upload' in image.local_path:
        path = image.local_path.replace('upload','output')
    else:
        path = str(image.local_path)+'/output'

    img.save(path , optimize=True , quality=int(image.quality),progressive=1,progression=1)

    return path





def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
