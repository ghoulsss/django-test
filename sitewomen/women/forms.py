from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, BaseValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Husband


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок', min_length=5,
                            widget=forms.TextInput(attrs={'class': 'form-input'}),
                            error_messages={'min_length': 'Слишком короткий заголовок',
                                            'required': 'Без заголовка никак'})
    slug = forms.SlugField(max_length=255, required=False, label='URL', validators=[
        MinLengthValidator(5, message='Минимум 5 символов'),
        MaxLengthValidator(100, message='Минимум 5 символов')
    ])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), label='Контент')
    is_published = forms.BooleanField(required=False, label='Статус', initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 label='Категории', empty_label='Категория не выбрана')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False,
                                     label='Муж', empty_label='Не замужем')

    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- '
        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError('Должны быть только русские символы, дефис или пробел')
