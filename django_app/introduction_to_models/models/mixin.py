from django.db import models
from utils.models.mixins import TimeStampedMixin

'''
Post모델
    author = User와 연결
    title
    content
    create_date
        DateTimeField사용
    modified_date
        DateTimeField사용
        
Comment모델
    author = User와 연결
    content
    create_date
    modified_date
    
User모델
    name
    created_date
    modified_date
'''


class User(TimeStampedMixin):
    name = models.CharField(max_length=50)


class Post(TimeStampedMixin):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()


class Comment(TimeStampedMixin):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField()
