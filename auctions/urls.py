from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auction/<str:id>", views.auction, name="auction"),
    path("auction/<str:id>/bid", views.auction_bid, name="auction_bid"),
    path("auction/<str:id>/close", views.auction_close, name="close_auction"),
    path("auction/<str:id>/comment", views.auction_comment, name="post_comment"),
    path("auction/<str:id>/watch", views.watch_auction, name="watch_auction"),
    path("categories", views.categories_list, name="categories"),
    path("categories/<str:name>", views.category, name="category"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watchlist", views.watchlist, name="watchlist")
]
