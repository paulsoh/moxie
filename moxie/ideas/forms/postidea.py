from django.forms import ModelForm

from django_summernote.widgets import SummernoteInplaceWidget

from ideas.models import Idea


class PostIdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = [
            'title',
            'description',
            'price',
            'sales_goal',
            'custom_slug',
            'end_date',
        ]
        widgets = {
            'description': SummernoteInplaceWidget(),
        }
