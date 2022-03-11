from django.contrib import admin
from django.urls import path
from    home.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_view,name='create'),
    path('search', search,name='search'),
    path('HomeView', HomeView.as_view() ,name='HomeView'),
    path('BikesView', BikesView.as_view() ,name='BikesView'),
    path('BajajView', BajajView.as_view() ,name='BajajView'),
    path('bajajiView', bajajiView.as_view() ,name='bajajiView'),
    path('MotoView', MotoView.as_view() ,name='MotoView'),
]
