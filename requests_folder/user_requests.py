import requests


class UserRequests:
    _BASE_URL = "https://gorest.co.in"
    _API_USERS_ENDPOINT = "/public/v2/users"
    _USERS_URL = _BASE_URL + _API_USERS_ENDPOINT
    API_TOKEN = "4279f84de4a2b0f69ae154912ed70b5abaf06b0ecf4d8d3579957997d2733174"
    MY_USER_ID = 5287678

    def get_all_users(self):
        response = requests.get(self._USERS_URL)
        return response

    def get_users_by_gender(self, gender):
        request_body = {
            "gender": gender
        }
        response = requests.get(self._USERS_URL, json=request_body)
        return response

    def get_users_by_status(self, status):
        request_body = {
            "status": status
        }
        response = requests.get(self._USERS_URL, json=request_body)
        return response

    def get_user_by_name(self, name, access_token):
        header_params = {
            "Authorization": f"Bearer {access_token}"
        }
        request_body = {
            "name": name
        }
        response = requests.get(self._USERS_URL, json=request_body, headers=header_params)
        return response

    def get_user_by_email(self, email, access_token):
        header_params = {
            "Authorization": f"Bearer {access_token}"
        }
        request_body = {
            "email": email
        }
        response = requests.get(self._USERS_URL, json=request_body, headers=header_params)
        return response

    def add_user(self, access_token, name, email, gender, status):
        header_params = {
            "Authorization": f"Bearer {access_token}"
        }
        request_body = {
            "name": name,
            "email": email,
            "gender": gender,
            "status": status
        }
        response = requests.post(self._USERS_URL, headers=header_params, json=request_body)
        return response

    def get_user_id_by_name(self, name):
        request_body = {
            "name": name
        }
        response = requests.get(self._USERS_URL, json=request_body)
        for i in range(len(response.json())):
            if response.json():
                id = response.json()[i]["id"]
                return id

    def get_user_id_by_email(self, email):
        request_body = {
            "email": email
        }
        response = requests.get(self._USERS_URL, json=request_body)
        for i in range(len(response.json())):
            if response.json():
                id = response.json()[i]["id"]
                return id

    def delete_user(self, name, access_token):  # functie pentru userii predefiniti de pe server
        user_id = self.get_user_id_by_name(name)
        delete_user_url = self._BASE_URL + self._API_USERS_ENDPOINT + f"/{user_id}"
        header_params = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.delete(delete_user_url, headers=header_params)
        return response

    def delete_my_user(self, user_id, access_token):  # functie pentru userul creat de mine, deoarece pe acesta nu il gaseste dupa "name"
        delete_user_url = self._BASE_URL + self._API_USERS_ENDPOINT + f"/{user_id}"
        header_params = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.delete(delete_user_url, headers=header_params)
        return response

    def get_my_user_details(self, user_id, access_token):
        my_user_details_url = self._BASE_URL + self._API_USERS_ENDPOINT + f"/{user_id}"
        header_params = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(my_user_details_url, headers=header_params)
        return response

    def modify_my_user_details(self, user_id, access_token, name, email, gender, status):
        my_user_url = self._BASE_URL + self._API_USERS_ENDPOINT + f"/{user_id}"
        header_params = {
            "Authorization": f"Bearer {access_token}"
        }
        request_body = {
            "name": name,
            "email": email,
            "gender": gender,
            "status": status
        }
        response = requests.put(my_user_url, headers=header_params, json=request_body)
        return response

    def modify_my_user_email_using_patch(self, user_id, access_token, email):
        my_user_url = self._BASE_URL + self._API_USERS_ENDPOINT + f"/{user_id}"
        header_params = {
            "Authorization": f"Bearer {access_token}"
        }
        request_body = {
            "email": email
        }
        response = requests.patch(my_user_url, json=request_body, headers=header_params)
        return response
