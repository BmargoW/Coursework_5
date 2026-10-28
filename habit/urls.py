from django.urls import path

from habit.views import HabitCreate, HabitList, HabitRetrieve, HabitUpdate, HabitDestroy

app_name = "habit"

urlpatterns = [
    path("habit/create/", HabitCreate.as_view(), name="h-create"),
    path("habit/list/", HabitList.as_view(), name="h-list"),
    path("habit/retrieve/<int:pk>/", HabitRetrieve.as_view(), name="h-retrieve"),
    path("habit/update/<int:pk>/", HabitUpdate.as_view(), name="h-update"),
    path("habit/delete/<int:pk>/", HabitDestroy.as_view(), name="h-delete"),
]
