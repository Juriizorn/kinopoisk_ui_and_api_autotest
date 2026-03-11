import requests


class SearchApi:

    def __init__(self, base_url: str, api_key: str, test_data: dict):
        self.__base_url = base_url
        self.__api_key = api_key
        self.__query = test_data

    def search_by_latin(self, search_req: str) -> dict:
        headers = {
            "X-API-KEY": self.__api_key
        }
        resp = requests.get("{kinopoisk}/v1.4/movie/search?page=1&limit=10"
                            "&query={query}".format
                            (kinopoisk=self.__base_url, query=search_req),
                            headers=headers)
        return resp.json()

    def search_by_cyrillic(self, search_req: str) -> dict:
        headers = {
            "X-API-KEY": self.__api_key
        }
        resp = requests.get("{kinopoisk}/v1.4/movie/search?page=1&limit=10"
                            "&query={query}".format
                            (kinopoisk=self.__base_url, query=search_req),
                            headers=headers)
        return resp.json()

    def search_by_numbers(self, search_req: str) -> dict:
        headers = {
            "X-API-KEY": self.__api_key
        }
        resp = requests.get("{kinopoisk}/v1.4/movie/search?page=1&limit=10"
                            "&query={query}".format
                            (kinopoisk=self.__base_url, query=search_req),
                            headers=headers)
        return resp.json()

    def search_by_arbitrary_set_of_letters(self, search_req: str) -> dict:
        headers = {
            "X-API-KEY": self.__api_key
        }
        resp = requests.get("{kinopoisk}/v1.4/movie/search?page=1&limit=10"
                            "&query={query}".format
                            (kinopoisk=self.__base_url, query=search_req),
                            headers=headers)
        return resp.json()

    def search_without_an_apikey(self, search_req: str):
        headers = {
            "X-API-KEY": ""
        }
        resp = requests.get("{kinopoisk}/v1.4/movie/search?page=1&limit=10"
                            "&query={query}".format
                            (kinopoisk=self.__base_url, query=search_req),
                            headers=headers)
        return resp
