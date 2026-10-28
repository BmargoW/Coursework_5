from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habit.models import UsefulHabit
from habit.pagination import MyPagination
from habit.permissions import PublicOrCarrierPerm
from habit.serializers import UsefulHabitSerializer


class HabitCreate(generics.CreateAPIView):
    serializer_class = UsefulHabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.carrier = self.request.user
        if new_habit.periodicity == "daily":
            new_habit.days_of_week = None
        new_habit.save()


class HabitList(generics.ListAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
    permission_classes = [PublicOrCarrierPerm]
    pagination_class = MyPagination

    def get_queryset(self):
        user = self.request.user
        qs = UsefulHabit.objects.all()

        if user.is_authenticated:
            qs = qs.filter(Q(publicity=True) | Q(carrier=user))
        else:
            qs = qs.filter(publicity=True)

        return qs


class HabitRetrieve(generics.RetrieveAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
    permission_classes = [PublicOrCarrierPerm]


class HabitUpdate(generics.UpdateAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
    permission_classes = [PublicOrCarrierPerm]


class HabitDestroy(generics.DestroyAPIView):
    queryset = UsefulHabit.objects.all()
    permission_classes = [PublicOrCarrierPerm]
