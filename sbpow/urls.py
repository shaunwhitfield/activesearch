from django.urls import path
from . import views

urlpatterns = [
    path('htmx/search/',views.htmx_search_view, name='htmx_search'),
    path('alpine/search/',views.alpine_search_view, name='alpine_search'),
    path('ajax/search/', views.ajax_search_view, name="ajax_search"),
    path('', views.home_view, name="home"),
]