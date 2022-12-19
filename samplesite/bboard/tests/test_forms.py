from bboard.forms import AdForm
from django.test import TestCase

from bboard.models import Rubric


class AdFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.rubric = Rubric.objects.create(name='Тестовая рубрика')

    def test_title_field_label(self):
        form = AdForm()
        self.assertTrue(
            form.fields['title'].label == 'Название товара'
        )

    def test_rubric_field_help_text(self):
        form = AdForm()
        self.assertEqual(
            form.fields['rubric'].help_text,
            'He забудьте задать рубрику!'
        )

    def test_ad_form_valid(self):
        form_data = {
            'title': 'title',
            'content': 'content',
            'price': 1.0,
            'rubric': self.rubric,
        }
        form = AdForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_ad_form_invalid_title(self):
        form_data = {
            'title': 'Прошлогодний снег',
            'content': 'content',
            'price': 1.0,
            'rubric': self.rubric,
        }
        form = AdForm(data=form_data)
        self.assertFalse(form.is_valid())