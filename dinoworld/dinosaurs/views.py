from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Category, Dinosaur


# Página principal
class HomeView(generic.ListView):

    model = Category

    template_name = "dinosaurs/index.html"

    context_object_name = "categories"


# Dinosaurios por categoría
class CategoryView(generic.DetailView):

    model = Category

    template_name = "dinosaurs/category.html"


# Detalle dinosaurio
class DinosaurDetailView(generic.DetailView):

    model = Dinosaur

    template_name = "dinosaurs/detail.html"


# Función votar
def vote(request, dinosaur_id):

    dinosaur = get_object_or_404(
        Dinosaur,
        pk=dinosaur_id
    )

    dinosaur.votes += 1

    dinosaur.save()

    return HttpResponseRedirect(
        reverse(
            "dinosaurs:detail",
            args=(dinosaur.id,)
        )
    )