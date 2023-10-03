import unittest

from requests_folder.user_requests import UserRequests


class TestCheckIfMyUserWasDeleted(unittest.TestCase):

    def setUp(self):
        self.users_api = UserRequests()
        self.my_user_id = self.users_api.MY_USER_ID
        self.access_token = self.users_api.API_TOKEN

    def test_check_that_my_user_was_deleted(self):
        response = self.users_api.get_my_user_details(self.my_user_id, self.access_token)
        expected_response_message = "Resource not found"
        actual_response_message = response.json()["message"]
        # print(actual_response_message)
        self.assertEqual(expected_response_message, actual_response_message, "Error, my user was not deleted")