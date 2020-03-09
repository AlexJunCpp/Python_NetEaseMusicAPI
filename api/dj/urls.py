from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path("banner", views.banner),
    path("hot", views.hot),
    path("hot/radio", views.hot_radio),
    path("detail", views.detail),
    path("pay", views.pay),
    path("program", views.program),
    path("program/detail", views.program_detail),
    path("program/toplist", views.program_toplist),
    path("program/toplist/hours", views.program_toplist_hours),
    path("streamer/hours", views.streamer_hours),
    path("streamer/newcomer", views.streamer_newcomer),
    path("streamer/hot", views.streamer_hot),
    path("toplist", views.toplist),
    path("catelist", views.catelist),
    path("recommend", views.recommend),
    path("recommend/type", views.recommend_type),
    path("category/recommend", views.category_recommend),
    path("category/excludehot", views.category_excludehot),
    path("sub", views.sub),
    path("sublist", views.sublist),
    path("paygift", views.paygift),
    path("today", views.today),
    path("djprogram", views.djprogram),
    path("program/recommend", views.program_recommend),
]
