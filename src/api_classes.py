from abc import ABC, abstractmethod
import requests
import os
from src.saver import JSONSaver


class APISample(ABC):

    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_json_saver(filename):
        return JSONSaver(filename)


class HHru(APISample):

    def __init__(self, keyword, page=0):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "text": keyword,
            "page": page
        }

    def get_request(self):
        return requests.get(self.url, params=self.params)


class SuperJob(APISample):

    def __init__(self, keyword, page=1):
        self.url = "https://api.superjob.ru/2.0/vacancies/"

        self.params = {
            "keywords": keyword,
            "page": page
        }

    def get_request(self):
        sj_secret_api_key = os.environ["SJ_SAP"]
        headers = {"X-Api-App-Id": sj_secret_api_key}
        return requests.get(self.url, headers=headers, params=self.params)
