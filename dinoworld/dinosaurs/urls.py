from django.urls import path

from . import views


app_name = "dinosaurs"


urlpatterns = [

    path(
        "",
        views.HomeView.as_view(),
        name="home"
    ),

    path(
        "category/<int:pk>/",
        views.CategoryView.as_view(),
        name="category"
    ),

    path(
        "dinosaur/<int:pk>/",
        views.DinosaurDetailView.as_view(),
        name="detail"
    ),

    path(
        "vote/<int:dinosaur_id>/",
        views.vote,
        name="vote"
    ),
]