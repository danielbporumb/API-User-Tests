import unittest

from requests_folder.user_requests import UserRequests


class TestModifyMyUserStatus(unittest.TestCase):

    def setUp(self):
        self.users_api = UserRequests()
        self.my_user_id = self.users_api.MY_USER_ID
        self.access_token = self.users_api.API_TOKEN

    def test_modify_my_user_status_using_put_status_code(self):
        name = "Fake User1"
        email = "fake_user1@test.example"
        gender = "male"
        status = "active"
        response = self.users_api.modify_my_user_details(self.my_user_id, self.access_token, name, email, gender, status)
        expected_response_code = 200
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code, "Error, the user detail was not modified")