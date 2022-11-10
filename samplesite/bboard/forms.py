from django import forms
from django.core.exceptions import ValidationError

from .models import Ad, Rubric


class AdForm(forms.ModelForm):
    title = forms.CharField(label='Название товара')
    content = forms.CharField(label='Описание', widget=forms.widgets.Textarea())
    price = forms.DecimalField(label='Цена', decimal_places=2)
    rubric = forms.ModelChoiceField(
        queryset=Rubric.objects.all(),
        label='Рубрика',
        help_text='He забудьте задать рубрику!',
        widget=forms.widgets.Select(attrs={'size': 8})
        )

    class Meta:
        model = Ad
        fields = ('title', 'content', 'price', 'rubric')

    def clean_title(self):
        val = self.cleaned_data['title']
        if val == 'Прошлогодний снег':
            raise ValidationError('К продаже не допускается')
        return val

    def clean(self):
        super().clean()
        errors = {}
        if not self.cleaned_data['content']:
            errors['content'] = ValidationError(
                'Укажите описание продаваемого товара'
            )
        if self.cleaned_data['price'] and self.cleaned_data['price'] < 0:
            errors['price'] = ValidationError(
                'Укажите неотрицательное значение цены'
            )
        if errors:
            raise ValidationError(errors)

        return self.cleaned_data
