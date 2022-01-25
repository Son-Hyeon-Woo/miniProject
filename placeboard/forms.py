from django import forms
# from .models import UploadFile


class BoardForm(forms.Form):
    postname = forms.CharField(error_messages = {'required':"제목을 입력해주세요"}, label = "제목", max_length=128)
    contents = forms.CharField(error_messages = {'required':"내용을 입력해주세요."}, label = "내용", widget = forms.Textarea)

# class UploadFileForm(foems.ModelForm):
#     class META:
#         model=UploadFile
#         fields=['file']