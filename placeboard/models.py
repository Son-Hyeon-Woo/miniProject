from django.db import models
from django.utils.timezone import now
# from member import models
  ####  pip install pillow  커맨드창에서 해줘야함
  # 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50,null=True)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(upload_to="", blank=True, null=True)
    contents = models.TextField()
    # writer= models.ForeignKey('Member', related_name='user_id', on_delete=models.CASCADE, db_column='user_id')
    # date=models.DateTimeField(default=now, editable=False)

    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname



# class Answer(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     content = models.TextField()
#     writer = models.CharField(max_length=20)
#     date = models.DateTimeField()

#     def __str__(self):
#         return self.title