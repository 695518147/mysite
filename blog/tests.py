from django.test import TestCase
from datetime import datetime
from django.test.client import Client
from blog.models import BlogPost


# Create your tests here.
class BlogPostTest(TestCase):
    def test_obj_crate(self):
        BlogPost.objects.create(title='test', body='test body', timestamp=datetime.now())
        self.assertEqual('test', BlogPost.objects.get(id=BlogPost.objects.count()).title)

    def test_home(self):
        response = self.client.get('/blog/')
        self.failUnlessEqual(response.status_code, 200)

    def test_slash(self):
        response = self.client.get('/')
        self.assertIn(response.status_code, (200,))

    def test_empty_create(self):
        response = self.client.get('/blog/create/')
        self.assertIn(response.status_code, (302, 301))

    def test_post_create(self):
        response = self.client.post('/blog/create/', {'title': 'post test', 'body': 'post test body'})
        self.assertIn(response.status_code, (301, 302))
        print(BlogPost.objects.get(id=BlogPost.objects.count()).title)
        self.assertEqual('post test', BlogPost.objects.get(id=BlogPost.objects.count()).title)
