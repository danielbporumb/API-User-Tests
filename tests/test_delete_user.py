import unittest

from requests_folder.user_requests import UserRequests


class TestDeleteUser(unittest.TestCase):

    def setUp(self):
        self.users_api = UserRequests()
        self.my_user_id = self.users_api.MY_USER_ID
        self.access_token = self.users_api.API_TOKEN

    def test_delete_user_status_code(self):
        response = self.users_api.delete_user("Chaturaanan Achari", self.access_token)
        expected_status_code = 204
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code, "Error, the user was not deleted")