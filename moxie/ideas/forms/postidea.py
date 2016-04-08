from django.forms import ModelForm

from django_summernote.widgets import SummernoteInplaceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset, ButtonHolder
from crispy_forms.bootstrap import FormActions

from ideas.models import Idea


class PostIdeaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostIdeaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create!'))
        self.helper.layout = Layout(
            Div(
                'title',
                'thumbnail_image',
            ),
            Fieldset(
                '두번째 단계',
                'price',
                'sales_goal',
                'end_date',
            ),
            Fieldset(
                '마지막 단계',
                'description',
                'custom_slug',
            ),
        )

    class Meta:
        model = Idea
        fields = [
            'title',
            'thumbnail_image',
            'description',
            'price',
            'sales_goal',
            'custom_slug',
            'end_date',
        ]
        widgets = {
            'description': SummernoteInplaceWidget(),
        }
