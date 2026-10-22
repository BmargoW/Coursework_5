
from rest_framework import generics

from habit.models import UsefulHabit
from habit.pagination import MyPagination
from habit.serializers import UsefulHabitSerializer


class HabitCreate(generics.CreateAPIView):
    serializer_class = UsefulHabitSerializer
   # permission_classes = [IsAuthenticated]


    # def perform_create(self, serializer):
    #     new_lesson = serializer.save()
    #     new_lesson.owner = self.request.user
    #     new_lesson.save()


class HabitList(generics.ListAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
    # permission_classes =  [IsAuthenticated]
    pagination_class = MyPagination


class HabitRetrieve(generics.RetrieveAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
    #permission_classes = [OwnerPerm|ModeratorPerm]

class HabitUpdate(generics.UpdateAPIView):
    serializer_class = UsefulHabitSerializer
    queryset = UsefulHabit.objects.all()
   # permission_classes = [OwnerPerm]

class HabitDestroy(generics.DestroyAPIView):
    queryset = UsefulHabit.objects.all()
   #permission_classes = [OwnerPerm]
