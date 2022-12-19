from django.test import TestCase
from django.urls import reverse

from bboard.models import Ad, Rubric


class AdListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_ad = 13
        rubric = Rubric.objects.create(name='Тестовая рубрика')
        for author_num in range(number_of_ad):
            Ad.objects.create(
                rubric=rubric,
                title='title',
                content='content',
                price=1.0,
            )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/bboard/list/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('space:list-class'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('space:list-class'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'bboard/index.html')

    def test_lists_all_ads(self):
        resp = self.client.get(reverse('space:list-class'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue( len(resp.context['ads']) == 13)