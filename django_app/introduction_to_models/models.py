from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    PERSON_TYPES = (
        ('student', '학생'),
        ('teather', '선생'),
    )
    person_type = models.CharField(
        '유형',
        max_length=10,
        choices=PERSON_TYPES,
        default=PERSON_TYPES[0][0],
    )
    # teacher속성 지정 (ForeignKey, 'self'를 이용해 자기 자신을 가리킴, null=True 허용)
    teacher = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    name = models.CharField('이름', max_length=60)
    shirt_size = models.CharField(
        '셔츠사이즈',
        max_length=1,
        choices=SHIRT_SIZES,
        help_text='남자는 L 쓰세요',
    )

# INSTALLED_APPS에 이 모델이 속하는 app 추가
# makemigiration로 migrations생성
# migrate로 migration 적용
# admin.py에 Person클래스 등록
# createsuperuser로 슈퍼유저 계정 생성
# runserver후 admin 접속해서Person 객체 생성 및 저장

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