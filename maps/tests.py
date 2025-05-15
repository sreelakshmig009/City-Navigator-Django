from django.test import TestCase
from django.contrib.auth.models import User
from .models import Map

class MapNavigationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser')
        self.map = Map.objects.create(
            owner=self.user,
            name="Test Map",
            layout=[
                ["R", "R", "R", "R"],
                ["#", "#", "R", "#"], 
                ["#", "#", "R", "R"],
                ["#", "#", "R", "#"]
            ]
        )

    def test_reachable_path(self):
        response = self.client.get(
            f'/maps/{self.map.id}/navigation/',
            {'start_row': 0, 'start_col': 0, 'end_row': 3, 'end_col': 2}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['path_exists'])

    def test_unreachable_path(self):
        response = self.client.get(
            f'/maps/{self.map.id}/navigation/',
            {'start_row': 0, 'start_col': 0, 'end_row': 3, 'end_col': 0}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()['path_exists'])