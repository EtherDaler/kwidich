import datetime

from django.db import models
from django.contrib.auth.models import User


def default_date():
    return datetime.date.today()


def default_datetime():
    return datetime.datetime.now()


class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    logo = models.ImageField(upload_to="mainApp/teams/logo/", verbose_name="Флаг", blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец", related_name="own", blank=True, null=True)
    coach = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Тренер", related_name="train")

    def __str__(self):
        return self.name


class Positions(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Команда")
    position = models.ForeignKey(Positions, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name="Позиция(роль)", related_name='players')
    strong_sides = models.TextField(verbose_name="Сильные стороны", null=True, blank=True)
    weak_sides = models.TextField(verbose_name="Слабые стороны", null=True, blank=True)
    illnesses = models.TextField(verbose_name="Болезни", null=True, blank=True)
    injuries = models.TextField(verbose_name="Травмы", null=True, blank=True)


class Game(models.Model):
    owners = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Хозяева", related_name="owners")
    guests = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Гости", related_name="guests")
    datetime = models.DateField(verbose_name="Дата и время", default=default_datetime())
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Победитель")


class Train(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Команда")
    date = models.DateField(verbose_name="Дата тренировки", default=default_date())


class MemberGames(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="Игрок")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="Игра")


class MemberTrains(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="Игрок")
    train = models.ForeignKey(Train, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Тренировка")
