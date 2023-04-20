from django.forms import ModelForm, TextInput, Select, Textarea

from .models import Posts


class CreatePost(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'category', 'text']

        widgets = {
            'title': TextInput(attrs={
                'id': 'text-title',
                'placeholder': 'Заголовок',
            }),
            'category': Select(attrs={
                'id': 'text-category',
                'placeholder': 'Категория'
            }),
            'text': Textarea(attrs={
                'id': 'text-content',
                'placeholder': 'Текст'
            }),
        }
