import requests

class APIManager:
    def __init__(self):
        self.GENDER_BASE_URL = "https://api.genderize.io?name="
        self.AGE_BASE_URL = "https://api.agify.io?name="
        self.BLOGS_URL = "https://api.npoint.io/c790b4d5cab58020d391"

    def rquest_info_by_name(self, name):
        gender_response = requests.get(self.GENDER_BASE_URL+name)
        age_response = requests.get(self.AGE_BASE_URL+name)
        gender = gender_response.json()["gender"]
        age = age_response.json()["age"]
        return gender, age

    def request_blogs(self):
        response = requests.get(self.BLOGS_URL)
        return response.json()

