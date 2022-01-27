# from xml.etree.ElementTree import Comment
from django import forms
from django.forms import ModelForm
from .models import *

class FileUploadForm(ModelForm):
    postname = forms.CharField(error_messages = {'required':"제목을 입력해주세요"}, label = "제목", max_length=128)
    contents = forms.CharField(error_messages = {'required':"내용을 입력해주세요."}, label = "내용", widget = forms.Textarea)
    mainphoto = forms.ImageField(error_messages = {'required':"사진을 입력해주세요."}, label = "사진")
    class Meta:
        model = Post
        fields = ['postname', 'mainphoto', 'contents']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']