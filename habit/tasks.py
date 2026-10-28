import os

import requests
from django.utils import timezone

# from django.core.mail import send_mail
from celery import shared_task
from collections import defaultdict


from .models import UsefulHabit

TELEGRAM_URL = "https://api.telegram.org/"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

WEEKDAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


@shared_task
def send_daily_habit():
    now = timezone.now()
    today_name = WEEKDAY_MAP[now.weekday()]

    habits = UsefulHabit.objects.filter(
        carrier__isnull=False,
    ).select_related("carrier")

    habits_by_user = defaultdict(list)

    for habit in habits:

        if habit.periodicity == "daily":
            habits_by_user[habit.carrier].append(habit)
            continue
        if not habit.days_of_week:
            continue
        if today_name not in habit.days_of_week:
            continue

        habits_by_user[habit.carrier].append(habit)

    for user, user_habits in habits_by_user.items():
        print("all ok")

        if not user.tg_chat_id:
            continue  # нет TG — не шлем

        # subject = "Ваши привычки на сегодня"
        lines = []
        for h in user_habits:
            line = f"- «{h.action}»"
            if h.reward:
                line += f", награда: {h.reward}"
            lines.append(line)
        text = "Сегодня запланированы следующие привычки:\n" + "\n".join(lines)

        send_message(text, user.tg_chat_id)


def send_message(text, chat_id):
    """функция отправки уведомления через телеграмм"""
    params = {
        "text": text,
        "chat_id": chat_id,
    }
    requests.get(f"{TELEGRAM_URL}bot{TELEGRAM_TOKEN}/sendMessage", params=params)
    try:
        resp = requests.get(
            f"{TELEGRAM_URL}bot{TELEGRAM_TOKEN}/sendMessage", params=params, timeout=10
        )
        resp.raise_for_status()
    except Exception as e:
        print(e)


#
#     # Отправляем письмо пользователю
#     for user, user_habits in habits_by_user.items():
#         if not user.email:
#             continue  # нет почты — не шлем
#
#         subject = "Ваши привычки на сегодня"
#         lines = []
#         for h in user_habits:
#             line = f"- «{h.action}»"
#             if h.reward:
#                 line += f", награда: {h.reward}"
#             lines.append(line)
#         message = "Сегодня запланированы следующие привычки:\n" + "\n".join(lines)
#
#         # send_mail(
#         #     subject=subject,
#         #     message=message,
#         #     from_email=None,
#         #     recipient_list=[user.email],
#         # )
#
#         print(message)


@shared_task()
def send_mail_about_hubit():
    """тестовая функция"""
    print("Hello")
