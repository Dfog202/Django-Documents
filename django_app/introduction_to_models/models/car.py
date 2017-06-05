from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=40)
    manufacturer = models.ForeignKey(
        Manufacturer,
        # 'Manufacturer',  더 뒤에서 지정됬을때 문자로 찾을수 있다.
        # myapp.Manufacurer,  이런방법으로 찾을수도 있다.
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name