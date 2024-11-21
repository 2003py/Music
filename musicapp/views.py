from django.shortcuts import render
from django.http import HttpResponse
from.models import Music
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')


def music_list_view(request):
    searchTerm = request.GET.get('searchMusic')
    if searchTerm:
        music_items = Music.objects.filter(name__icontains=searchTerm)
    else:
        music_items = Music.objects.all()

    # 创建Paginator对象，设置每页显示2首歌曲
    paginator = Paginator(music_items, 2)
    page_number = request.GET.get('page')
    # 获取指定页码的页面内容，如果没有指定页码，默认显示第一页
    page_obj = paginator.get_page(page_number)

    context = {
       'page_obj': page_obj,  # 将包含分页信息和对应页面音乐数据的page_obj传递给模板
       'searchTerm': searchTerm
    }
    return render(request,'music_list.html', context)
def signup(request):  # 定义视图函数 signup
    email = request.GET.get('email')  # 从 GET 请求中获取邮箱
    return render(request, 'signup.html', {'email': email})



