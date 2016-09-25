from django.conf.urls import url

from trends import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^fetch_and_draw_data/', views.fetch_and_draw_data, name='fetch_and_draw_data'),
]