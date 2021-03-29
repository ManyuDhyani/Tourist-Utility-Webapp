from django.shortcuts import render
from .models import City
from .forms import cityForm
from .utils import get_weather_data, get_city_news, get_city_images

def home(request):
    weather_data = {}
    news_data_list = {}
    images_data_list = {}
    if request.method == 'POST':
        form = cityForm(request.POST)
        if form.is_valid():
            form.save()
            city = form.cleaned_data.get('city')
            if 'weather' == request.POST.get('query'):
                weather_data = get_weather_data(city)
            elif 'news' == request.POST.get('query'):
                news_data_list = get_city_news(city)
            elif 'images' == request.POST.get('query'):
                images_data_list = get_city_images(city)
    else:
        form = cityForm()
        try:
            city = City.objects.latest('data_added').city
            weather_data = get_weather_data(city)
        except Exception as e:
            weather_data = None

    context = {
        'form': form,
        'weather_data': weather_data,
        'news_data_list': news_data_list,
        'images_data_list': images_data_list
    }
    return render(request, "home.html", context)


def history(request):
    cities = City.objects.all().order_by('-data_added')[:5]
    weather_data_list = []
    for city in cities:
        city_name = city.city
        weather_data_list.append(get_weather_data(city_name))
    return render(request, "history.html", {'weather_data_list': weather_data_list})