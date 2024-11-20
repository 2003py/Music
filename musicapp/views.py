from django.shortcuts import render
from django.http import HttpResponse
from.models import Music
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
    return render(request, 'home.html')

def musichome(request):
    searchTerm = request.GET.get('searchMusic')
    if searchTerm:
        music_list = Music.objects.filter(name__icontains=searchTerm)
    else:
        music_list = Music.objects.all()
    # 固定每页显示数量为2，无论数据总量如何，都每页显示两首音乐
    per_page_num = 3
    paginator = Paginator(music_list, per_page_num)
    page_number = request.GET.get('page')
    try:
        musics = paginator.page(page_number)
    except PageNotAnInteger:
        musics = paginator.page(1)
    except EmptyPage:
        # 处理空页情况
        if paginator.num_pages > 0:
            musics = paginator.page(paginator.num_pages)
        else:
            empty_message = "没有找到符合条件的音乐，请尝试更换搜索关键词或查看其他内容。"
            return render(request,'musichome.html', {'empty_message': empty_message})

    return render(request,'musichome.html', {'searchTerm': searchTerm,'music': musics})