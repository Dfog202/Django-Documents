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
