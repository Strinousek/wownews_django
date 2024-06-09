from django.shortcuts import render
from .utils import parse_news_from_wowhead

# Create your views here.

def index(request):
    news = parse_news_from_wowhead(10)
    context = {
        "pageTitle": "Home",
        "news": news
    }
    return render(request, "index.html", context)

def about_us(request):
    return render(request, "about_us.html", {
        "pageTitle": "About Us",
    })