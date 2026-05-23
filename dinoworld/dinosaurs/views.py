from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages

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


# CREAR dinosaurio
class DinosaurCreateView(generic.CreateView):

    model = Dinosaur

    fields = ["name", "description", "image", "category"]

    template_name = "dinosaurs/create.html"

    success_url = reverse_lazy("dinosaurs:home")



# UPDATE
class DinosaurUpdateView(generic.UpdateView):

    model = Dinosaur

    fields = ["name", "description", "image"]

    template_name = "dinosaurs/detail.html"

    def form_valid(self, form):

        messages.success(
            self.request,
            "Dinosaurio actualizado correctamente"
        )

        return super().form_valid(form)

    def get_success_url(self):

        return reverse_lazy(
            "dinosaurs:detail",
            kwargs={"pk": self.object.id}
        )


# DELETE
class DinosaurDeleteView(generic.DeleteView):

    model = Dinosaur

    success_url = reverse_lazy("dinosaurs:home")

    def delete(self, request, *args, **kwargs):

        messages.success(
            request,
            "Dinosaurio eliminado correctamente"
        )

        return super().delete(
            request,
            *args,
            **kwargs
        )

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