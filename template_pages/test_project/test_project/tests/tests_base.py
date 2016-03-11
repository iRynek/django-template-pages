# -*- coding: utf-8 -*-
from distutils.version import StrictVersion

from django import get_version as get_django_version
from django.test import TestCase
from django.test.utils import override_settings

if StrictVersion(get_django_version()) >= StrictVersion('1.9.0'):
    from django.template.exceptions import TemplateDoesNotExist
else:
    from django.template import TemplateDoesNotExist


@override_settings(
    TEMPLATE_PAGES_CONTEXT_MODULE=None,
    DEBUG=False
)
class TestRoutingView(TestCase):
    _template_pages_test_context_module = 'test_project.template_pages_context'

    def test_file(self):
        response = self.client.get('/test1/')
        self.assertContains(response, 'This is test1.')

    @override_settings(
        TEMPLATE_PAGES_CONTEXT_MODULE=_template_pages_test_context_module
    )
    def test_file_with_context(self):
        response = self.client.get('/test1/')
        self.assertContains(response, 'Hello World!')

    def test_index(self):
        response = self.client.get('/')
        self.assertContains(response, 'This is index.')

    @override_settings(
        TEMPLATE_PAGES_CONTEXT_MODULE=_template_pages_test_context_module
    )
    def test_index_with_context(self):
        response = self.client.get('/')
        self.assertContains(response, 'Hello World!')

    def test_directory_index(self):
        response = self.client.get('/test2/')
        self.assertContains(response, 'This is test2 index.')

    @override_settings(
        TEMPLATE_PAGES_CONTEXT_MODULE=_template_pages_test_context_module
    )
    def test_directory_index_with_context(self):
        response = self.client.get('/test2/')
        self.assertContains(response, 'Hello World!')

    def test_file_inside_directory(self):
        response = self.client.get('/test2/test3/')
        self.assertContains(response, 'This is test2/test3.')

    @override_settings(
        TEMPLATE_PAGES_CONTEXT_MODULE=_template_pages_test_context_module
    )
    def test_file_inside_with_context(self):
        response = self.client.get('/test2/test3/')
        self.assertContains(response, 'Hello World!')

    def test_unicode_path(self):
        response = self.client.get(u'/django-wymiąta/'.encode('utf-8'))
        self.assertEqual(response.status_code, 404)

    def test_dir_up(self):
        response = self.client.get('/../index/')
        self.assertEqual(response.status_code, 404)

    def test_same_dir(self):
        response = self.client.get('/./test2/')
        self.assertEqual(response.status_code, 404)

    def test_redirect_wo_trailing_slash(self):
        response = self.client.get('/test2')
        self.assertRedirects(response, '/test2/', status_code=301)

    @override_settings(
        DEBUG=True
    )
    def test_not_supressing_errors_in_debug(self):
        with self.assertRaises(TemplateDoesNotExist):
            self.client.get('/test-rocket-cat-does-not-exists/')

    @override_settings(
        DEBUG=False
    )
    def test_supressing_errors_not_in_debug(self):
        response = self.client.get('/test-rocket-cat-does-not-exists/')
        self.assertEqual(response.status_code, 404)
