from django.urls import path
from .views import home_view,post_detail_view,about_view,fashion_view,travel_view


urlpatterns=[
    path('',home_view,name='home_view'),
    path('about/<slug:slug>/',post_detail_view,name='about'),
    path('about/', about_view, name='about_page'),
    path('fashion/', fashion_view, name='fashion'),
    path('travel/', travel_view, name='travel'),
]