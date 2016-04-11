from django.forms import ModelForm

from django_summernote.widgets import SummernoteInplaceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset, ButtonHolder
from crispy_forms.bootstrap import FormActions

from ideas.models import Idea


class UpdateIdeaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateIdeaForm, self).__init__(*args, **kwargs)

        self.fields['title'].label = "아이디어 제목"
        self.fields['thumbnail_image'].label = "대표 이미지"
        self.fields['price'].label = "판매 가격"
        self.fields['sales_goal'].label = "목표 판매량"
        self.fields['end_date'].label = "모집 종료일"
        self.fields['custom_slug'].label = "URL 설정"
        self.fields['description'].label = "아이디어 상세 설명"

        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                HTML("""
                    <h3>기본 정보</h3>
                """),
                Field('title'),
                Field('thumbnail_image'),
                css_id='step-1',
            ),
            Div(
                HTML("""
                    <h3>아이디어 기본 정보</h3>
                """),
                'price',
                HTML("""
                <input type="text" id="price-slider" class="span2" \
                        data-slider-min="1000" data-slider-max="250000" \
                        data-slider-step="1000">
                """),
                'sales_goal',
                HTML("""
                <input type="text" id="goal-slider" class="span2" \
                        data-slider-min="20" data-slider-max="200" \
                        data-slider-step="5">
                """),
                HTML("""
                <div id="expected-sales">예상 매출:</div>
                """),
                'end_date',
                css_id='step-2',
            ),
            Div(
                HTML("""
                    <h3>아이디어 상세 설명</h3>
                """),
                'custom_slug',
                'description',
                css_id='step-3',
            ),
            Div(
                Submit('submit', 'Update!'),
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
