from django.urls import path
from . import views

urlpatterns = [
    path('htmx/search/',views.htmx_search_view, name='htmx_search'),
    path('ajax/search/', views.ajax_search_view, name="ajax_search"),
]