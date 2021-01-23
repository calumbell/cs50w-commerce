from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auction/<str:id>", views.auction, name="auction"),
    path("auction/<str:id>/bid", views.auction_bid, name="auction_bid"),
    path("auction/<str:id>/comment", views.auction_comment, name="post_comment"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
