from django.db import models
from django.conf import settings


  ####  pip install pillow  커맨드창에서 해줘야함
  # 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50,null=True)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    writer=models.CharField(max_length=20, null=True)
    date=models.DateTimeField()

    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.CharField(max_length=20, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.postname

