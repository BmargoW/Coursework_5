from datetime import timedelta

from rest_framework import serializers

from habit.models import UsefulHabit



class UsefulHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsefulHabit
        fields = "__all__"

    def validate_duration(self, value):

        if value is not None and value < timedelta(minutes=2):
            raise serializers.ValidationError("Время выполнения должно быть не меньше двух минут.")
        return value


    def validate(self, data):

        niceaction = data.get('niceaction')
        reward = data.get('reward')
        sign_pleasantness = data.get('sign_pleasantness')
        action = data.get('action')

        if niceaction is not None:
            # Каждый раз запрашиваем актуальные данные из БД
            existing_actions = set(
                UsefulHabit.objects.filter(sign_pleasantness=True).values_list('action', flat=True)
            )
            if niceaction not in existing_actions:
                raise serializers.ValidationError({
                    "niceaction": "В связанные привычки могут попадать только привычки с признаком приятности."
                })

        if niceaction and reward:
            raise serializers.ValidationError({
                "reward": "Не может быть заполнено одновременно вознаграждение и приятное действие. Выберите что-то одно."
            })

        if niceaction and reward:
            raise serializers.ValidationError({
                "reward": "не может быть заполнено поле вознаграждения, если выбрана приятная привычка"
            })

        if reward and niceaction:
            raise serializers.ValidationError({
                "niceaction": "не может быть заполнено поле приятной привыяки, если выбрано вознаграждение"
            })

        if sign_pleasantness is not False and reward:
            raise serializers.ValidationError({
                "reward": "Приятная привычка не должна иметь вознаграждение."
            })

        if sign_pleasantness is True and niceaction:
            raise serializers.ValidationError({
                "niceaction": "Приятная привычка не должна иметь связанную приятную привычку."
            })

        return data