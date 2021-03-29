from django.contrib import admin
from django.urls import path
from Dashboard.views import home, history

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('history/', history, name='history'),
]
