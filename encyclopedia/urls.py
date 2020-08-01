from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path('', views.index, name='index'),
    path('wiki/<str:title>', views.entry, name='entry'),
    path('search', views.search, name='search'),
    path('new_page', views.new, name='new'),
    path('save', views.save, name='save')
]
