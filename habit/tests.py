from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase, APIClient
from habit.models import UsefulHabit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="Drug", email="drug@mail.ru")
        self.habit = UsefulHabit.objects.create(place="лекторий",  action="лекция",
                                            carrier=self.user)
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habit:h-retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        print(data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("action"), "лекция"
        )

    def test_habit_create(self):
        url = reverse("habit:h-create")
        data = {
            "place": "Татами",
            "action": "растяжка",

        }

        response = self.client.post(url, data, format="json")
        print("Status:", response.status_code)
        print("Response JSON:", response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_data = response.json()

        self.assertEqual(created_data.get("place"), "Татами")

    def test_habit_update(self):
        url = reverse("habit:h-update", args=(self.habit.pk,))

        data = {
            "place": "институт",

        }
        response = self.client.patch(url)
        print("Status:", response.status_code)
        print("Response JSON:", response.json())

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("place"), "институт"
        )

    def test_habit_delete(self):
        url = reverse("habit:h-delete", args=(self.habit.pk,))

        response = self.client.delete(url)
        print("Status:", response.status_code)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

    def test_habit_list(self):
        url = reverse("habit:h-list")

        response = self.client.get(url)

        print("Status:", response.status_code)
        print("Response JSON:", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)


