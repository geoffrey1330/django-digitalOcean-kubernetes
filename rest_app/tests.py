from django.test import TestCase
from . models import Article


class ModelTesting(TestCase):

    def setUp(self):
        self.article = Article.objects.create(title='boy', author='michael')

    def test_contact_model(self):
        d = self.article
        self.assertTrue(isinstance(d, Article))
        self.assertEqual(str(d), 'boy')