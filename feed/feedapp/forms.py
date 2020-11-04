from django.forms import ModelForm, Textarea, TextInput

from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        widgets = {
            'text': TextInput(attrs={'class' : 'input', 'placeholder' : 'Say something...'}),
        }