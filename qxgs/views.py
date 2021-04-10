from .models import QXgs
from django.http import JsonResponse
from .serializers import Qxgs_DetailSerializer, Qxgs_ListSerializer
# Create your views here.

def qxgs_list(request):

    content = dict()

    gs_list = QXgs.objects\
        .values('id','qxgs_name','simple_content','img')
    
    s = Qxgs_ListSerializer(instance=gs_list, many=True)

    content['qxgs_list'] = s.data

    return JsonResponse(content, json_dumps_params={'ensure_ascii':False})

def qxgs_detail(request,name_id):

    content = dict()
    qx_content = QXgs.objects\
            .filter(id=name_id)\
            .values('qxgs_name','content','img')

    s = Qxgs_DetailSerializer(instance=qx_content, many=True)
    content['qxgs_detail'] = s.data

    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})


