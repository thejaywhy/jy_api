import requests

from django.test import TestCase, LiveServerTestCase

from jy_api.apps.api.models import (
    Link,
    Role,
    Task,
    Interest
)

class BaseViewTest(TestCase):
    """
    Common test setup
    """


    @classmethod
    def setUpTestData(cls):
        """
        Set up some data in the database
        """
        #super(BaseViewTest, cls).setUpClass()
        cls.role = Role.objects.create(
            name="role1",
            description="a role"
        )
        cls.link = Link.objects.create(
            name="link1",
            description="a link",
            link_url="http://example.com/test/"
        )
        cls.task = Task.objects.create(
            name="task1",
            description="a task",
            role=cls.role
        )
        cls.interest = Interest.objects.create(
            name="interest1",
            description="an interest",
            role=cls.role
        )

    def get_html(self, uri):
        """
        get an HTML representation of the given URI
        """
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        }

        return requests.get(
            url=self.live_server_url + uri,
            headers=headers
        )

    def assert_html(self, uri, response):
        """
        Validate response is HTML
        """
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.headers['Content-Type'])
        self.assertIn('<b>GET</b> {}'.format(uri), response.text)


    def get_json(self, uri):
        """
        get an JSON representation of the given URI
        """
        headers = {
            "Accept": "application/json"
        }

        return requests.get(
            url=self.live_server_url + uri,
            headers=headers
        )

    def assert_json(self, response):
        """
        Validiate response is JSON
        """
        self.assertEqual(response.status_code, 200)
        self.assertIn("application/json", response.headers['Content-Type'])
        self.assertIsNotNone(response.json())

class JSONAPITest(BaseViewTest, LiveServerTestCase):
    """
    Tests that a client can navigate the API
    """

    def assert_list_header(self, count, json):
        """
        check for common json "header" data
        """
        self.assertIn("count", json)
        self.assertEqual(count, json["count"])
        self.assertIn("previous", json)
        self.assertIn("next", json)
        self.assertIn("results", json)
        self.assertIsNotNone(json["results"])

    def assert_has_common_fields(self, json):
        """
        verify that a JSON object has the common fields
        """
        self.assertIn("id", json)
        self.assertIn("created", json)
        self.assertIn("url", json)
        self.assertIn("name", json)
        self.assertIn("description", json)

    def test_site_root(self):
        """
        Test for when a client requests JSON at root
        """
        response = self.get_json('/')
        self.assert_json(response)
        json = response.json()
        self.assertIn('links', json)
        self.assertIn('roles', json)
        self.assertIn('tasks', json)
        self.assertIn('interests', json)

    def test_site_links(self):
        """
        Test for when a client requests JSON at /links/
        """
        response = self.get_json('/links/')
        self.assert_json(response)
        json = response.json()
        self.assert_list_header(1, json)

    def test_site_link(self):
        """
        Test for when a client requests a specific Link
        """
        uri = '/links/link1/'
        response = self.get_json(uri)
        self.assert_json(response)
        json = response.json()

        self.assert_has_common_fields(json)

        self.assertIn("link_url", json)

        self.assertEqual(self.live_server_url + uri, json["url"])
        self.assertEqual(self.link.name, json["name"])
        self.assertEqual(self.link.description, json["description"])
        self.assertEqual(self.link.link_url, json["link_url"])

    def test_site_roles(self):
        """
        Test for when a client requests JSON at /roles/
        """
        response = self.get_json('/roles/')
        self.assert_json(response)

    def test_site_role(self):
        """
        Test for when a client requests a specific Role
        """
        uri = '/roles/role1/'
        response = self.get_json(uri)
        self.assert_json(response)
        json = response.json()

        self.assert_has_common_fields(json)

        self.assertEqual(self.live_server_url + uri, json["url"])
        self.assertEqual(self.role.name, json["name"])
        self.assertEqual(self.role.description, json["description"])

    def test_site_tasks(self):
        """
        Test for when a client requests JSON at /tasks/
        """
        response = self.get_json('/tasks/')
        self.assert_json(response)

    def test_site_task(self):
        """
        Test for when a client requests a specific Task
        """
        uri = '/tasks/task1/'
        role_uri = '/roles/{}/'.format(self.task.role.name)
        response = self.get_json(uri)
        self.assert_json(response)
        json = response.json()

        self.assert_has_common_fields(json)

        self.assertEqual(self.live_server_url + uri, json["url"])
        self.assertEqual(self.task.name, json["name"])
        self.assertEqual(self.task.description, json["description"])
        self.assertIn("role", json)
        self.assertEqual(self.live_server_url + role_uri, json["role"])

    def test_site_interests(self):
        """
        Test for when a client requests JSON at /interests/
        """
        response = self.get_json('/interests/')
        self.assert_json(response)

    def test_site_interest(self):
        """
        Test for when a client requests a specific Interest
        """
        uri = '/interests/interest1/'
        role_uri = '/roles/{}/'.format(self.interest.role.name)
        response = self.get_json(uri)
        self.assert_json(response)
        json = response.json()

        self.assert_has_common_fields(json)

        self.assertEqual(self.live_server_url + uri, json["url"])
        self.assertEqual(self.interest.name, json["name"])
        self.assertEqual(self.interest.description, json["description"])
        self.assertIn("role", json)
        self.assertEqual(self.live_server_url + role_uri, json["role"])


class BrowsableTest(BaseViewTest, LiveServerTestCase):
    """
    Tests that a web browser can navigate the API
    """

    def test_site_root(self):
        # user opens web browser, navigates to site root
        uri = '/'
        response = self.get_html(uri)
        self.assert_html(uri, response)

    def test_site_links(self):
        # user opens web browser, navigates to links page
        uri = '/links/'
        response = self.get_html(uri)
        self.assert_html(uri, response)

    def test_site_roles(self):
        # user opens web browser, navigates to roles page
        uri = '/roles/'
        response = self.get_html(uri)
        self.assert_html(uri, response)

    def test_site_tasks(self):
        # user opens web browser, navigates to tasks page
        uri = '/tasks/'
        response = self.get_html(uri)
        self.assert_html(uri, response)

    def test_site_interests(self):
        # user opens web browser, navigates to interests page
        uri = '/interests/'
        response = self.get_html(uri)
        self.assert_html(uri, response)

    def test_site_interactive(self):
        # user opens web browser, navigates to interests page
        uri = '/interactive/'
        response = self.get_html(uri)
        self.assertEqual(200, response.status_code)
        self.assertIn("Swagger", response.text)
