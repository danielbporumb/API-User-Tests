import unittest

from requests_folder.user_requests import UserRequests


class TestCheckIfMyUserWasModified(unittest.TestCase):

    def setUp(self):
        self.users_api = UserRequests()
        self.my_user_id = self.users_api.MY_USER_ID
        self.access_token = self.users_api.API_TOKEN

    def test_check_if_my_user_parameter_was_modified_using_put(self):
        response = self.users_api.get_my_user_details(self.my_user_id, self.access_token)
        expected_user_status = "active"
        actual_user_status = response.json()["status"]
        # print(actual_user_status)
        self.assertEqual(expected_user_status, actual_user_status, "Error, the status of the user was not modified")

    def test_check_if_my_user_email_was_modified_using_patch(self):
        response = self.users_api.get_my_user_details(self.my_user_id, self.access_token)
        expected_user_email = "fake_user1_modified@test.example"
        actual_user_email = response.json()["email"]
        print(actual_user_email)
        self.assertEqual(expected_user_email, actual_user_email, "Error, the emails of the user was not modified")