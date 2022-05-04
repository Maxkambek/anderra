from django import forms
from .models import Comment


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def __int__(self, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name


