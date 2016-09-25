from django.conf.urls import include, url

urlpatterns = [
    url(r'^trends/', include('trends.urls'))
]