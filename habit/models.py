from django.db import models

from users.models import User


# Create your models here.

class UsefulHabit(models.Model):
    FREQUENCY_CHOICES = [
        ('once_week', '1 раз в неделю'),
        ('twice_week', '2 раза в неделю'),
        ('thrice_week', '3 раза в неделю'),
        ('four times a week', '4 раза в неделю'),
        ('daily', 'Ежедневно'),
    ]

    carrier = models.ForeignKey(
        User,

        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="носитель",
    )
    place = models.CharField(max_length=50, verbose_name="пространство")
    time = models.TimeField(null=True, blank=True)
    action = models.CharField(max_length=50, verbose_name="полезная привычка")
    sign_pleasantness= models.BooleanField(default=False, verbose_name="приятность")
    niceaction = models.CharField(max_length=50, verbose_name="приятная привычка", blank=True)
    periodicity = models.CharField(max_length=50, choices=FREQUENCY_CHOICES, default='daily', verbose_name="периодичность")
    reward = models.CharField(max_length=50, verbose_name="вознаграждение", blank=True)
    duration = models.DurationField(null=True, blank=True)
    publicity = models.BooleanField(default=False, verbose_name="публичность")


    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["action"]