from django.forms import ModelForm

from django_summernote.widgets import SummernoteInplaceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset, ButtonHolder
from crispy_forms.bootstrap import FormActions

from ideas.models import Idea


class PostIdeaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostIdeaForm, self).__init__(*args, **kwargs)

        self.fields['title'].label = "아이디어 제목"
        self.fields['category'].label = "아이디어 카테고리"
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
                Field('title', css_class="form-control"),
                Field('category', css_class="form-control"),
                Field('thumbnail_image'),
                css_id='step-1',
            ),
            Div(
                HTML("""
                    <h3>아이디어 기본 정보</h3>
                """),
                Field('price', css_class="form-control"),
                HTML("""
                <input type="text" id="price-slider" class="span2 form-control" \
                        data-slider-min="1000" data-slider-max="250000" \
                        data-slider-step="1000">
                """),
                Field('sales_goal', css_class="form-control"),
                HTML("""
                <input type="text" id="goal-slider" class="span2 form-control" \
                        data-slider-min="20" data-slider-max="200" \
                        data-slider-step="5">
                """),
                HTML("""
                <div id="expected-sales">예상 매출:</div>
                """),
                Field('end_date', css_class="form-control"),
                css_id='step-2',
            ),
            Div(
                HTML("""
                    <h3>아이디어 상세 설명</h3>
                """),
                Field('custom_slug', css_class="form-control"),
                HTML("""
                    <p>올바른 URL형태로 입력해주세요. 입력하지 않으시면 자동으로 생성됩니다.</p>
                """),
                'description',
                css_id='step-3',
            ),
            Div(
                Button('prev', '이전'),
                Button('next', '다음'),
                Submit('submit', 'Create!'),
            ),
        )

    class Meta:
        model = Idea
        fields = [
            'title',
            'category',
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
