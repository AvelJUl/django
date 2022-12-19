from django.test import TestCase
from bboard.models import Ad, Rubric


class AdModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        rubric = Rubric.objects.create(name='Тестовая рубрика')
        Ad.objects.create(
            rubric=rubric,
            title='title',
            content='content',
            price=1.0,
        )

    def test_rubric_label(self):
        ad = Ad.objects.get(id=1)
        field_label = ad._meta.get_field('rubric').verbose_name
        self.assertEquals(field_label, 'Рубрика')

    def test_title_label(self):
        ad = Ad.objects.get(id=1)
        field_label = ad._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Заголовок')

    def test_title_max_length(self):
        ad = Ad.objects.get(id=1)
        max_length = ad._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)

    def test_object_name(self):
        ad = Ad.objects.get(id=1)
        expected_object_name = f'{ad.published} {ad.title}'
        self.assertEquals(expected_object_name, str(ad))

    def test_get_absolute_url(self):
        ad = Ad.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(ad.get_absolute_url(), '/bboard/detail/1/')