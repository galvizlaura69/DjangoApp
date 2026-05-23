from django.test import TestCase
from django.urls import reverse

from .models import Category, Dinosaur


class DinosaurViewsTest(TestCase):

    def setUp(self):

        self.category = Category.objects.create(
            name="Carnívoros"
        )

        self.dinosaur = Dinosaur.objects.create(
            name="T-Rex",
            description="Dinosaurio feroz",
            image="https://imagen.com/trex.jpg",
            category=self.category,
            votes=0
        )



    def test_home_view_status_code(self):

        response = self.client.get(
            reverse("dinosaurs:home")
        )

        self.assertEqual(
            response.status_code,
            200
        )



    def test_detail_view_shows_dinosaur(self):

        response = self.client.get(
            reverse(
                "dinosaurs:detail",
                args=[self.dinosaur.id]
            )
        )

        self.assertContains(
            response,
            "T-Rex"
        )



    def test_update_dinosaur(self):

        response = self.client.post(
            reverse(
                "dinosaurs:update",
                args=[self.dinosaur.id]
            ),
            {
                "name": "T-Rex Editado",
                "description": "Nueva descripción",
                "image": "https://imagen.com/new.jpg"
            }
        )

        self.dinosaur.refresh_from_db()

        self.assertEqual(
            self.dinosaur.name,
            "T-Rex Editado"
        )


    def test_delete_dinosaur(self):

        response = self.client.post(
            reverse(
                "dinosaurs:delete",
                args=[self.dinosaur.id]
            )
        )

        self.assertEqual(
            Dinosaur.objects.count(),
            0
        )

    # =========================
    # VOTE FUNCTION
    # =========================

    def test_vote_function(self):

        self.client.post(
            reverse(
                "dinosaurs:vote",
                args=[self.dinosaur.id]
            )
        )

        self.dinosaur.refresh_from_db()

        self.assertEqual(
            self.dinosaur.votes,
            1
        )