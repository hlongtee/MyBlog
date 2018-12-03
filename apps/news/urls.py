from django.urls import path
from news import views

app_name = 'news'
# <a href="{% url 'index' %}" ></a>
# <a href="{% url 'news:index' %}" ></a>

urlpatterns = [
    path('', views.index,name='news'),
]
