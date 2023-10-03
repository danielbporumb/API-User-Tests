import unittest

from requests_folder.user_requests import UserRequests


class TestGetAllUsers(unittest.TestCase):

    def setUp(self):
        self.users_api = UserRequests()

    def test_get_all_users_status_code(self):
        response = self.users_api.get_all_users()
        expected_response_code = 200
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected status code")

    def test_get_all_users_number_of_results(self):
        response = self.users_api.get_all_users()
        expected_number_of_results = 10
        actual_number_of_results = len(response.json())
        self.assertEqual(expected_number_of_results, actual_number_of_results, "Error, number users doesn't match")

    def test_get_all_male_users_status_code(self):
        response = self.users_api.get_users_by_gender("male")
        expected_response_code = 200
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected status code")

    def test_get_all_male_users_number_of_results(self):
        response = self.users_api.get_users_by_gender("male")
        expected_number_of_results = 10
        actual_number_of_results = len(response.json())
        self.assertEqual(expected_number_of_results, actual_number_of_results, "Error, number of male users doesn't match")

    def test_get_all_female_users_status_code(self):
        response = self.users_api.get_users_by_gender("female")
        expected_response_code = 200
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected status code")

    def test_get_all_female_users_number_of_results(self):
        response = self.users_api.get_users_by_gender("female")
        expected_number_of_results = 10
        actual_number_of_results = len(response.json())
        self.assertEqual(expected_number_of_results, actual_number_of_results, "Error, number of female users doesn't match")

    def test_get_all_active_users_status_code(self):
        response = self.users_api.get_users_by_status("active")
        expected_response_code = 200
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected status code")

    def test_get_all_active_users_number_of_results(self):
        response = self.users_api.get_users_by_status("active")
        expected_number_of_results = 10
        actual_number_of_results = len(response.json())
        self.assertEqual(expected_number_of_results, actual_number_of_results, "Error, number of active users doesn't match")

    def test_get_all_inactive_users_status_code(self):
        response = self.users_api.get_users_by_status("inactive")
        expected_response_code = 200
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected status code")

    def test_get_all_inactive_users_number_of_results(self):
        response = self.users_api.get_users_by_status("inactive")
        expected_number_of_results = 10
        actual_number_of_results = len(response.json())
        self.assertEqual(expected_number_of_results, actual_number_of_results, "Error, number of inactive users doesn't match")