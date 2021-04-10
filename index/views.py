from django.http import JsonResponse
from .models import SYImg
from .serializers import Syimg_IndexSerializer

def syimg_index(request):

    content = dict()

    imgs = SYImg.objects.order_by("-published_time")[0:5].values("img")
    
    s = Syimg_IndexSerializer(instance=imgs, many=True)

    content['syimg_index'] = s.data

    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})