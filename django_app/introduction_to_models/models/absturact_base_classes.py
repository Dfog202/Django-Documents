from django.db import models
from .car import Car


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    cars = models.ManyToManyField(
        Car,
        related_name="%(app_label)s_%(class)ss",
        related_query_name="%(app_label)s_%(class)s",
    )

    # cars필드에 MTM으로
    # related_name, related_query_name을 설정 후 migrate

    class Meta:
        abstract = True
        ordering = ['-name', ]


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return 'HomeGroup {}\'s student({}, {})'.format(
            self.home_group,
            self.name,
            self.age,
        )

    class Meta:
        db_table = 'introducion_to_models_abc_student'


class Teacher(CommonInfo):
    cls = models.CharField(max_length=20)

    def __str__(self):
        return 'Class {} \'s teacher ({}, {})'.format(
            self.cls,
            self.name,
            self.age,
        )

    class Meta:
        db_table = 'introducion_to_models_abc_teacher'
