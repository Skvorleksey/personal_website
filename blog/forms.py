from django.forms import ModelForm
from .models import BlogPost


class PostUpdateForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ('text',)
        exclude = ('publication_date_time',)
