import unittest

from requests_folder.user_requests import UserRequests


class TestGetUserDetails(unittest.TestCase):

    def setUp(self):
        self.users_api = UserRequests()
        self.my_user_id = self.users_api.MY_USER_ID
        self.access_token = self.users_api.API_TOKEN

    def test_get_user_id_by_name(self):
        expected_id = 5285782
        actual_id = self.users_api.get_user_id_by_name(name="Mahesh Pillai")
        # print(actual_id)
        self.assertEqual(expected_id, actual_id, "Error, user id doesn't match")

    def test_get_user_id_by_email(self):
        expected_id = 5285781
        actual_id = self.users_api.get_user_id_by_email(email="mishra_dayaanidhi@sauer-spinka.example")
        # print(actual_id)
        self.assertEqual(expected_id, actual_id, "Error, user id doesn't match")

    def test_get_user_all_details_by_name(self):
        response = self.users_api.get_user_by_name("Aanand Dhawan", self.access_token)
        expected_user_email = "dhawan_aanand@lemke-ziemann.test"
        user_details = response.json()[0]["email"]  # ma intereseaza primul user gasit si ce se afla la atributul email,
        # deoarece am ales sa verific prin compararea emailului
        # print(user_details)
        self.assertIn(expected_user_email, user_details, "Error, the details requested for that name doesn't match")

    def test_get_user_all_details_by_email(self):
        response = self.users_api.get_user_by_email("cpa_johar_anang@leffler.example", self.access_token)
        expected_user_name = "Anang Johar CPA"
        user_details = response.json()[0]["name"]  # ma intereseaza primul user gasit si ce se afla la atributul name,
        # deoarece am ales sa verific prin compararea name-ului
        # print(user_details)
        self.assertIn(expected_user_name, user_details, "Error, the details requested for that email doesn't match")



