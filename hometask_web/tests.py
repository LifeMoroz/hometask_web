from unittest import TestCase

from django.http import HttpResponse
from django.test import Client
from mock import mock

from hometask_web.mappers import PCMapper


class MyCase(TestCase):

    def test_pcview(self):
        with mock.patch('django.shortcuts.render_to_response', return_value=HttpResponse()) as mock_foo:
            c = Client()
            resp = c.get("/")
            self.assertEqual(resp.status_code, 200)

        self.assertIn('pc_list.html', mock_foo.call_args[0])
        self.assertIn('pcs', mock_foo.call_args[0][1])

    def test_pcmapper(self):
        class X:
            def fetchall(self):
                return (1, '1234'),

        with mock.patch('db.db.SqlLite3.execute', return_value=X()) as m:
            mapper = PCMapper()
            obj = mapper.select()[0]
            self.assertIsInstance(obj, mapper.model)
            self.assertEqual(obj.title, '1234')
            self.assertEqual(obj.id, 1)
        m.assert_called_once()
