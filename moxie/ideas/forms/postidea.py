from django.forms import ModelForm

from django_summernote.widgets import SummernoteInplaceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions

from ideas.models import Idea


class PostIdeaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostIdeaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create!'))

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
