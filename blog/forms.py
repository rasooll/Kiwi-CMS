from django.forms import ModelForm, Textarea, TextInput
from .models import Comment

class SendComment(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }