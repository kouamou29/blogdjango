from django.forms import ModelForm, forms

from src.models import Post


class FormBlog(ModelForm):


    class Meta:
        model = Post
        fields = ['name', 'description', ]


