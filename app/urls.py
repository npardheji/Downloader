
from django.urls import path,include
from app import views
urlpatterns = [
    path('',views.home,name="home"),
    path('yt-home',views.new_home,name="ythome"),
    #path('yt-download',views.ytDownload,name='yt-download')
]
