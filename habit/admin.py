from django.contrib import admin
from .models import UsefulHabit


@admin.register(UsefulHabit)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ("action", "sign_pleasantness", "niceaction", "reward")


