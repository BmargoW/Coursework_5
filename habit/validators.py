# from rest_framework.exceptions import ValidationError
#
# from habit.models import UsefulHabit
#
#
# actions_2 = UsefulHabit.objects.filter(sign_pleasantness = True)
# actions = actions_2.values_list('action', flat=True)
#
#
# def niceaction_validator(value):
#
#     if value not in actions:
#         raise ValidationError("в связанные привычки могут попадть только привычки с признаком приятности")