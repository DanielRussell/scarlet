from cms import bundles, views

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from models import *

import datetime
import unittest

class BundleViewsTestCase(TestCase):
    def setup_test_user(self):
        user = User.objects.create_user('tester', 'tester@example.com', '1234')
        user.is_staff = True
        user.save()
        self.client.login(username='tester', password='1234')
        self.user = user

    def setUp(self):
        self.client = Client()
        self.setup_test_user()

        author = Author.objects.create(
                    name='Joe Tester',
                    bio='I like testing.'
                )

        # Create a category
        category = Category.objects.create(
                    category='Category Test',
                    slug='category_test'
                )

        # Create  a post
        self.post = Post.objects.create(
                    date=datetime.datetime.now(),
                    title='Title Test',
                    slug='Slug Test',
                    body='This is a test body for the post object.',
                    author=author,
                    category=category,
                    keywords='keywords test',
                    description='This is a test description for the post object.'
                )

        # Create a post image
        post_image = PostImage.objects.create(
                    post=self.post,
                    caption='This is a test caption for the post image object.'
                )

        # create a comment
        comment = Comment.objects.create(
                    post=self.post,
                    name='Test Commenter',
                    text='Test comment.  Great blog post!'
                )

    def test_list(self):
        resp = self.client.get('/admin/blog/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('list' in resp.context)
        self.assertEqual([row.instance.id for row in resp.context['list']], [self.post.pk])

    def test_add(self):
        resp = self.client.get('/admin/blog/add/')
        self.assertEqual(resp.status_code, 200)

    def test_edit(self):
        resp = self.client.get('/admin/blog/%s/edit/' % self.post.pk)
        self.assertEqual(resp.status_code, 200)

    def test_delete(self):
        resp = self.client.get('/admin/blog/%s/edit/delete/' % self.post.pk)
        self.assertEqual(resp.status_code, 200)


class TestMainBundle(bundles.Bundle):
    navigation = bundles.PARENT
    main = views.ListView(display_fields=('user', 'text'))

    class Meta:
        primary_model_bundle = True


class TestBundle1(TestMainBundle):
    navigation = bundles.PARENT

    class Meta:
        primary_model_bundle = True


class TestBundle2(TestMainBundle):
    navigation = bundles.PARENT
    dashboard = (('main',),
         ('tv_main', 'Landing Page',
                    {'adm_tv_pk': 'tv_main'}),)

    class Meta:
        primary_model_bundle = True




class BundleTestCase(unittest.TestCase):

    def setUp(self):
        self.tbm = TestMainBundle(name='test-main',title='Test main Title',
                    title_plural='Test main Titles',
                    parent=None, attr_on_parent=None, site=None)

        self.tb1 = TestBundle1(name='test1',title='Test1 Title', title_plural='Test1 Titles',
                    parent=None, attr_on_parent=None, site=None)

        self.tb2 = TestBundle2(name='test2',title='Test2 Title', title_plural='Test2 Titles',
                    parent=None, attr_on_parent=None, site=None)


    def test_bundles(self):

        self.tb1.name = 'test1 change'
        self.assertEquals( self.tb1.name, 'test1 change')
        self.assertEquals( self.tb2.name, 'test2')
        self.assertEquals( self.tbm.name, 'test-main')

        self.tbm.title = '333'
        self.assertEquals( self.tb1.title, 'Test1 Title')
        self.assertEquals( self.tb2.title, 'Test2 Title')
        self.assertEquals( self.tbm.title, '333')

        self.tb2.dashboard = (('main'),)
        self.assertEquals( self.tb1.dashboard, ())
        self.assertEquals( self.tb2.dashboard, (('main'),))
        self.assertEquals( self.tbm.dashboard, ())
