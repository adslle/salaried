from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.

from .models import BU
from django.urls import reverse


class AuthorListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass
        # Create 13 authors for pagination tests
        # number_of_bu = 13
        # for bu_num in range(number_of_bu):
        #     BU.objects.create(name='Name %s' % bu_num, description='Description %s' % bu_num,manager='Manager %s' % bu_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/bu/')
        self.assertEqual(resp.status_code, 200)

    # def test_view_url_accessible_by_name(self):
    #     resp = self.client.get(reverse('bu.index'))
    #     self.assertEqual(resp.status_code, 200)
    #
    # def test_view_uses_correct_template(self):
    #     resp = self.client.get(reverse('bu.index'))
    #     self.assertEqual(resp.status_code, 200)
    #
    #     self.assertTemplateUsed(resp, 'bu/index.html')
    #
    # def test_pagination_is_ten(self):
    #     resp = self.client.get(reverse('bu.index'))
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertTrue('is_paginated' in resp.context)
    #     self.assertTrue(resp.context['is_paginated'] == True)
    #     self.assertTrue(len(resp.context['author_list']) == 5)
    #
    # def test_lists_all_bu(self):
    #     # Get second page and confirm it has (exactly) remaining 3 items
    #     resp = self.client.get(reverse('bu.index') + '?page=2')
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertTrue('is_paginated' in resp.context)
    #     self.assertTrue(resp.context['is_paginated'] == True)
    #     self.assertTrue(len(resp.context['author_list']) == 5)