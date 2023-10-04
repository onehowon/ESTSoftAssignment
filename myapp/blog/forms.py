# blog/forms.py
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):

		class Meta:
				model = Post
				fields = ['content']