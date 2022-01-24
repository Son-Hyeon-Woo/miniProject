from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    date = models.DateTimeField()

    postname = models.CharField(max_length=50,null=True)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    writer=models.CharField(max_length=20, null=True)
    date=models.DateTimeField()

    def __str__(self):
        return self.title

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.CharField(max_length=20, null=True)
    date = models.DateTimeField()

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    date = models.DateTimeField()
    def __str__(self):
        return self.postname

    def __str__(self):
        return self.title