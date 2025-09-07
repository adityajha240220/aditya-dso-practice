from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import News
from .forms import NewsForm

def home(request):
    latest_five = News.objects.order_by("-created_at")[:5]
    return render(request, "baap/home.html", {"latest_five": latest_five})

def news_list(request):
    order = request.GET.get("order", "-created_at")
    all_news = News.objects.all().order_by(order)
    return render(request, "baap/list.html", {"all_news": all_news, "order": order})

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, "baap/detail.html", {"news": news})

def news_today(request):
    today = timezone.now().date()
    qs = News.objects.filter(created_at__date=today).order_by("-created_at")
    return render(request, "baap/today.html", {"today_news": qs})

def news_category(request, name):
    qs = News.objects.filter(category=name).order_by("-created_at")
    return render(request, "baap/category.html", {"items": qs, "name": name})

def news_create(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect("news_detail", slug=instance.slug)
    else:
        form = NewsForm()
    return render(request, "baap/create.html", {"form": form})
