from utils.pager import Page_Info
from .models import XXgk_GG, XXgk_RC 
from django.http import JsonResponse
from django.utils import timezone
from django.core.cache import cache
from .serializers import GgSerializer
# Create your views here.


def rczp_detail(request):

    content = dict()
    new_content = dict()
    content_list = list()
    xx_content = XXgk_RC.objects\
                .order_by("-published_time")\
                .values("content","published_time")

    new_content['published_time'] = str(xx_content[0]['published_time'])
    new_content['content'] = xx_content[0]["content"]

    content_list.append(new_content)
    content['rczp_detail'] = content_list

    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})

def jtgg_index(request):
    
    content = dict()

    xx_content = XXgk_GG.objects\
                .order_by("-published_time")\
                .values('id','title','published_time')\
                [0:13]

    s = GgSerializer(instance=xx_content, many=True)

    content['jtgg_index'] = s.data

    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})



def jtgg_list(request):

    content = dict()

    all_pager = cache.get("XXgk_GG_count")

    if (all_pager==None):
        all_pager = XXgk_GG.objects.all().count()
        cache.set("XXgk_GG_count", all_pager, None)

    page_info = Page_Info(request.GET.get('page'),all_pager,10)

    xx_content = XXgk_GG.objects\
                .order_by("-published_time")\
                .values('id','title','published_time')\
                [page_info.start:page_info.end]

    s = GgSerializer(instance=xx_content, many=True)

    content['page'] = page_info.get_pager()
    content['jtgg_list'] = s.data

    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})

def jjgg_detail(request,jt_pk):

    content = dict()
    new_content = dict()
    content_list = list()
    xx_content = XXgk_GG.objects\
                .filter(pk=jt_pk)\
                .values('title','content','published_time')

    new_content['title'] = xx_content[0]['title']
    new_content['content'] = xx_content[0]['content']
    new_content['published_time'] = str(xx_content[0]['published_time'])

    content_list.append(new_content)
    
    content['jjgg_detail'] = content_list

    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})

