from .models import GYwm, GYwm_XX, GYwm_GC
from django.http import JsonResponse
from .serializers import GywmSerializer
# Create your views here.


def gywm_list(request,type_name):

    content = dict()
    new_content = dict()
    content_list = list()
    gy_content = GYwm.objects.filter(gywm_type=type_name)

    # print(gy_content[0].get_gywm_type_display())
    new_content['content'] = gy_content[0].content

    content_list.append(new_content)
    content[type_name] = content_list

    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})

def jtgc_list(request):

    content = dict()

    gy_content = GYwm_GC.objects.values("content","img")

    s = GywmSerializer(instance=gy_content, many=True)

    content['jtgc_list'] = s.data

    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})

def ppxx_list(request):

    content = dict()

    gy_content = GYwm_XX.objects.values("content","img")

    s = GywmSerializer(instance=gy_content, many=True)

    content['ppxx_list'] = s.data

    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})

