import requests
from django.conf import settings


def get_weather_data(city):
    url = f'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': settings.OWM_API_KEY,
        'units': 'metric',
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return

    json_response = response.json()

    weather_data = {
        'temp': json_response['main']['temp'],
        'temp_min': json_response['main']['temp_min'],
        'temp_max': json_response['main']['temp_max'],
        'city_name': json_response['name'],
        'country': json_response['sys']['country'],
        'lat': json_response['coord']['lat'],
        'lon': json_response['coord']['lon'],
        'weather': json_response['weather'][0]['main'],
        'weather_desc': json_response['weather'][0]['description'],
        'pressure': json_response['main']['pressure'],
        'humidity': json_response['main']['humidity'],
        'wind_speed': json_response['wind']['speed'],
    }

    return weather_data

def get_city_news(city):
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/NewsSearchAPI"

    querystring = {
        "q": city,
        "pageNumber": "1",
        "pageSize": "9",
        "autoCorrect": "true",
        "fromPublishedDate": "null",
        "toPublishedDate": "null",
        "safeSearch": "true",
        "withThumbnails": "true",
        "thumbnailHeight": 202,
        "thumbnailWidth": 202
    }

    headers = {
        'x-rapidapi-key': settings.WS_API_KEY,
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code != 200:
        return

    json_response = response.json()

    if json_response['value'] == []:
        return None

    news_data_list = []
    for i in range(0, 9):
        news_data = {
            'title': json_response['value'][i]['title'],
            'url': json_response['value'][i]['url'],
            'description': json_response['value'][i]['description'],
            'datePublished': json_response['value'][i]['datePublished'],
            'image': json_response['value'][i]['image']['thumbnail']
        }

        news_data_list.append(news_data)
    return news_data_list

def get_city_images(city):

    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"

    querystring = {
        "q": city,
        "pageNumber": "1",
        "pageSize": "11",
        "autoCorrect": "true",
        "safeSearch": "true",
    }

    headers = {
        'x-rapidapi-key': settings.WS_API_KEY,
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code != 200:
        return

    json_response = response.json()

    if json_response['value'] == []:
        return None

    images_data_list = []
    for i in range(0, 9):
        image_data = {
            'title': json_response['value'][i]['title'],
            'url': json_response['value'][i]['url'],
            'image': json_response['value'][i]['thumbnail']
        }

        images_data_list.append(image_data)

    return images_data_list