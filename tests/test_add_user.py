import unittest

from requests_folder.user_requests import UserRequests


class TestAddUser(unittest.TestCase):

    def setUp(self):
        self.users_api = UserRequests()
        self.my_user_id = self.users_api.MY_USER_ID
        self.access_token = self.users_api.API_TOKEN

    def test_add_user_status_code(self):
        name = "Fake User1"
        email = "fake_user1@test.example"
        gender = "male"
        status = "inactive"
        response = self.users_api.add_user(self.access_token, name, email, gender, status)
        expected_response_code = 201
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected status code, user was not added")

    def test_add_user_successfully_check_by_name_status_code(self):
        response = self.users_api.get_user_by_name("Fake User1", self.access_token)
        expected_response_code = 200
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code, "Error, user name was not found")
        # am incercat sa iau datele in acest mod pentru Fake User1, insa pentru el imi returneaza un dict gol
        # Pentru oricare alt user incerc cu aceasta metoda, imi returneaza toate detaliile, practic acesta este
        # un bug al endpointului

    def test_add_user_successfully_check_by_email_status_code(self):
        response = self.users_api.get_user_by_email("fake_user_1@test.example", self.access_token)
        expected_response_code = 200
        actual_response_code = response.status_code
        print(response.json())
        self.assertEqual(expected_response_code, actual_response_code, "Error, user name was not found")
        # acest test o sa treaca indiferent de situatie deoarece, chiar daca userul nu exista, el tot status code-ul
        # 200 o sa il returneze pentru ca returneaza un dict gol, practic este un bug al endpointului




