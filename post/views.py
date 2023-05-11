from django.shortcuts import render
from .models import Post

# from django.views.generic import ListView, DetailView

import requests


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, "posts.html", {"posts": posts})


# class Index(ListView):
#     model = Post
#     template_name = "index.html"
#     context_object_name = "posts"


# class PostDetail(DetailView):
#     model = Post
#     template_name = "posts.html"
#     context_object_name = "posts"


def weather(request):
    if request.method == "POST":
        city = request.POST["city"]
        # res = urllib.request.urlopen(
        #     "http://api.openweathermap.org/data/2.5/weather?q="
        #     + city
        #     + "&appid=cb771e45ac79a4e8e2205c0ce66ff633"
        # ).read()
        key = "&appid=cb771e45ac79a4e8e2205c0ce66ff633"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}{key}"
        res = requests.get(url)
        json_data = res.json()
        data = {
            "country_code": str(json_data["sys"]["country"]),
            "coordinate": str(json_data["coord"]["lon"])
            + ", "
            + str(json_data["coord"]["lat"]),
            "pressure": str(json_data["main"]["pressure"]),
            "temp": str(json_data["main"]["temp"]) + "K",
            "pressure": str(json_data["main"]["pressure"]),
            "humidity": str(json_data["main"]["humidity"]),
        }
        print(data)
        context = {
            "data": data,
        }

    else:
        city = ""
        context = {}
    return render(request, "weather.html", context=context)
