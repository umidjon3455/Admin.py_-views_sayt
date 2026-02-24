from django.shortcuts import render, get_object_or_404
from .models import Category, News


# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list': news_list
    }

    return render(request, "news/news_list.html", context=context)

def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, "news/news_detail.html", context=context)

def home_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    # Katta kapsula uchun oxirgi 3 ta
    minix_news = News.published.order_by('-publish_time')[:3]

    # O'zbekiston kategoriyasidan oxirgi 4 ta
    uzb_news = News.published.filter(
        category__name="Uzbekiston"
    ).order_by('-publish_time')[:4]

    context = {
        'news_list': news_list,
        'minix_news': minix_news,
        'uzb_news': uzb_news,
    }

    return render(request, "news/index.html", context)

#def home_page(request):
#    news_list = News.objects.filter(status=News.Status.Published),
#    minix_news = News.published.all().order_by('-publish_time')[:3],
#    uzb_news_1 = News.published.all().filter(category__name='Uzbekiston').order_by('-publish_time')[0],
#     uzb_news_2 = News.published.all().filter(category__name='Uzbekiston').order_by('-publish_time')[1],
#     uzb_news_3 = News.published.all().filter(category__name='Uzbekiston').order_by('-publish_time')[2],
#     uzb_news_4 = News.published.all().filter(category__name='Uzbekiston').order_by('-publish_time')[3],
#
#     context = {
#         'news_list': news_list,
#         'minix_news': minix_news,
#         'uzb_news_1': uzb_news_1,
#         'uzb_news_2': uzb_news_2,
#         'uzb_news_3': uzb_news_3,
#         'uzb_news_4': uzb_news_4,
#     }
#
#     return render(request, "news/index.html", context=context)


def uzb_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list': news_list
    }

    return render(request, "news/uzb.html", context=context)

def jahon_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list': news_list
    }

    return render(request, "news/single.html", context=context)

def school_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list': news_list
    }

    return render(request, "news/contact.html", context=context)