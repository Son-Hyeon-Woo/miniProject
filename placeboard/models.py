from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import os
from django.conf import settings
import sqlite3
conn = sqlite3.connect ('db.sqlite3',check_same_thread=False)
c = conn.cursor()
# from member import models
  ####  pip install pillow  커맨드창에서 해줘야함
  # 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50,null=True)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(upload_to="", blank=True, null=True)
    contents = models.TextField()
    writer= models.ForeignKey(User,related_name='posts', on_delete=models.CASCADE, null=True)
    date=models.DateTimeField(default=now, editable=False)
    # hits = models.PositiveIntegerField(verbose_name='조회수', default=0)
    # top_fixed = models.BooleanField(verbose_name='상단고정', default=False)

    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname

        #그림파일 같이삭제
    def delete(self, *args, **kargs):
        if self.mainphoto:
            path_photo=self.mainphoto
            print(path_photo)
            os.remove(os.path.join(settings.MEDIA_ROOT, self.mainphoto.path))
                  
        super(Post, self).delete(*args, **kargs)
        c.execute("DELETE FROM placeboard_post WHERE mainphoto='%s'"%path_photo)
        conn.commit()  

class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.TextField()
    writer = models.ForeignKey(User,related_name='comments', on_delete=models.CASCADE, null=True,)
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.comment
    