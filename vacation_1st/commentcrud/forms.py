from django import forms
from .models import Comment

class CommentForm(forms.Form):
    #class Meta: 위에 forms.ModelForm 이었음
        #model = Comment
        #fields = ['content']
        name = forms.CharField()
        email = forms.EmailField()
        files = forms.FileField()
        comment = forms.CharField(widget=forms.Textarea)