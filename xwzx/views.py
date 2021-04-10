from .models import JTNew, IMGNew
from django.http import JsonResponse
# Create your views here.
from django.utils import timezone
from utils.pager import Page_Info
from django.core.cache import cache
from .serializers import Img_IndexSerializer, Jj_IndexSerializer


def news_detail(New,New_name,new_pk):

    content = dict()
    new_content = dict()
    content_list = list()
    new = New.objects.filter(pk=new_pk).values()
    
    new_content['title'] = new[0]['title']
    new_content['author'] = new[0]['author']
    if(New_name=='imgnew_detail'):
        new_content['img'] = str(new[0]['img'])
    new_content['content'] = new[0]['content']
    new_content['published_time'] = str(new[0]['published_time'])

    content_list.append(new_content)

    content[New_name] = content_list

    return content


def jtnew_index(request):
    
    content = dict()
    
    jt_content = JTNew.objects\
        .order_by('-published_time')\
        .values('id','title','published_time')[0:13]
    
    s = Jj_IndexSerializer(instance=jt_content, many=True)
    content["jtnew_index"] = s.data

    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})


def jtnew_list(request):

    content = dict()
    
    all_pager = cache.get("JTNew_count")

    if (all_pager==None):
        all_pager = JTNew.objects.all().count()
        cache.set("JTNew_count", all_pager, None)

    page_info = Page_Info(request.GET.get('page'),\
        all_pager,20)
    
    jt_content = JTNew.objects\
        .order_by('-published_time')\
        .values('id','title','published_time')\
        [page_info.start:page_info.end]
    
    s = Jj_IndexSerializer(instance=jt_content, many=True)
    
    content['page'] = page_info.get_pager()
    content['jtnew_list'] = s.data
    
    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})


def jtnew_detail(request,JTNew_pk):

    content = news_detail(JTNew,'jtnew_detail',JTNew_pk)

    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})


def imgnew_index(request):

    content = dict()

    img_content = IMGNew.objects\
        .order_by("-published_time")\
        .values('id','title','img')[0:5]

    s = Img_IndexSerializer(instance=img_content, many=True)

    content['imgnew_index'] = s.data

    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})


def imgnew_list(request):

    content = dict()
    
    all_pager = cache.get("IMGNew_count")
    if (all_pager==None):
        all_pager = IMGNew.objects.all().count()
        cache.set("IMGNew_count", all_pager, None)

    page_info = Page_Info(request.GET.get('page'),\
        all_pager,13)
    
    img_content = IMGNew.objects\
        .order_by('-published_time')\
        .values('id','title','img')\
        [page_info.start:page_info.end]
    
    s = Img_IndexSerializer(instance=img_content, many=True)
    
    content['page'] = page_info.get_pager()
    content['imgnew_list'] = s.data
    
    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})


def imgnew_detail(request,IMGNew_pk):

    content = news_detail(IMGNew,'imgnew_detail',IMGNew_pk)

    return JsonResponse(content,json_dumps_params={'ensure_ascii':False})


