from django import forms

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostIdeaForm(forms.Form):
    description_input = forms.CharField(
        widget=SummernoteInplaceWidget(),
    )
