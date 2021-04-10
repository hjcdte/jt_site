from .models import Cp, Cp_Type
from .serializers import CP_IndexSerializer, CP_Type_ListSerializer, CP_Type_DetailSerializer
from django.http import JsonResponse
# Create your views here.

def cp_index(request):

    content = dict()

    index_list = Cp.objects\
                .filter(option=1)\
                .order_by("-created_time")\
                .values('id','cp_name','cp_type__cp_type','img')
    
    s = CP_IndexSerializer(instance=index_list, many=True)

    content['cp_index'] = s.data

    return JsonResponse(content, json_dumps_params={'ensure_ascii':False})


def cp_type_list(request):

    content = dict()
    cp_type = Cp_Type.objects.values('id','img','cp_type','content')
    # cp_list = CpyFw.objects.filter(option=1).order_by("-created_time")
    
    # cp_list = cp_type.cpyfw_set.all()
    s = CP_Type_ListSerializer(instance=cp_type, many=True)
    
    content["cp_type_list"] = s.data

    return JsonResponse(content, json_dumps_params={'ensure_ascii':False})

def cp_type_detail(request,cp_type_pk):
    content = dict()

    cp_type = Cp_Type.objects.filter(id=cp_type_pk)
    cp_list = cp_type[0].cp_set.values('id','cp_name','cp_type','img')

    s = CP_Type_DetailSerializer(instance=cp_list, many=True)
    
    content['cp_type_detail'] = s.data

    return JsonResponse(content, json_dumps_params={'ensure_ascii':False})

def cp_detail(request,cp_pk):
    content = dict()
    cp_content = dict()
    content_list = list()

    cp = Cp.objects.filter(pk=cp_pk)

    cp_content['cp_name'] = cp[0].cp_name
    cp_content['cp_type'] = str(cp[0].cp_type)
    cp_content['img'] = str(cp[0].img)
    cp_content['content'] = cp[0].content

    content_list.append(cp_content)
    content['cp_detail'] = content_list

    return JsonResponse(content, json_dumps_params={'ensure_ascii':False})
