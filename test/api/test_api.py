import allure
import pytest

from api.SearchApi import SearchApi


@pytest.mark.api
@allure.story("Тестирование поиска через API.")
@allure.title("Тест поиска по латинице.")
def test_search_by_latin(base_url: str, api_key: str, test_data: dict) -> None:
    api = SearchApi(base_url, api_key, test_data)
    resp = api.search_by_latin(test_data.get("api_search_1"))
    list_of_films = resp["docs"]
    first_movie = list_of_films[0]

    assert first_movie["alternativeName"] == test_data.get("api_search_1")


@pytest.mark.api
@allure.story("Тестирование поиска через API.")
@allure.title("Тест поиска по кириллице.")
def test_search_by_cyrillic(base_url: str, api_key: str,
                            test_data: dict) -> None:
    api = SearchApi(base_url, api_key, test_data)
    resp = api.search_by_latin(test_data.get("api_search_2"))
    list_of_films = resp["docs"]
    first_movie = list_of_films[0]

    assert first_movie["name"] == test_data.get("api_search_2")


@pytest.mark.api
@allure.story("Тестирование поиска через API.")
@allure.title("Тест поиска по цифрам.")
def test_search_by_numbers(base_url: str, api_key: str,
                           test_data: dict) -> None:
    api = SearchApi(base_url, api_key, test_data)
    resp = api.search_by_numbers(test_data.get("api_search_3"))
    list_of_films = resp["docs"]
    year_first_movie = list_of_films[0]

    assert str(year_first_movie["year"]) == test_data.get("api_search_3")


@pytest.mark.api
@allure.story("Тестирование поиска через API.")
@allure.title("Тест поиска по произвольному набору букв.")
def test_search_by_arbitrary_set_of_letters(base_url: str, api_key: str,
                                            test_data: dict):
    api = SearchApi(base_url, api_key, test_data)
    resp = (api.search_by_arbitrary_set_of_letters
            (test_data.get("api_search_4")))
    list_of_films = resp["docs"]

    assert len(list_of_films) == 0


@pytest.mark.api
@allure.story("Тестирование поиска через API.")
@allure.title("Тест поиска без токена.")
def test_search_without_an_apikey(base_url: str, api_key: str,
                                  test_data: dict):
    api = SearchApi(base_url, api_key, test_data)
    resp = api.search_without_an_apikey("api_search_5")
    message = resp.json()

    assert message["message"] == "В запросе не указан токен!"
    assert resp.status_code == 401
