import unittest

from requests_folder.user_requests import UserRequests


class TestGetMyUserDetails(unittest.TestCase):

    def setUp(self):
        self.users_api = UserRequests()
        self.my_user_id = self.users_api.MY_USER_ID
        self.access_token = self.users_api.API_TOKEN

    def test_get_my_user_details_response_code(self):
        response = self.users_api.get_my_user_details(self.my_user_id, self.access_token)
        expected_response_code = 200
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code, "Error, wrong status code")
        # user_details = response.json()
        # print(user_details)

    def test_get_my_user_details_email_check(self):
        response = self.users_api.get_my_user_details(self.my_user_id, self.access_token)
        expected_user_email = "fake_user1@test.example"
        actual_email = response.json()["email"] # nu mai trebuie specificat intre [] al catelea rezultat ma intereseaza,
        # deoarece caut direct in dict-ul de pe url-ul userului meu
        # print(actual_email)
        self.assertEqual(expected_user_email, actual_email, "Error, requested details doesn't match")