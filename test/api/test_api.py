import allure

from api.SearchApi import SearchApi


@allure.story("Тестирование строки поиска через API.")
@allure.title("Тест на поиск по латинице.")
def test_search_by_latin(base_url: str, api_key: str, test_data: dict) -> None:
    api = SearchApi(base_url, api_key, test_data)
    resp = api.search_by_latin(test_data.get("api_search_1"))
    list_of_films = resp["docs"]
    first_movie = list_of_films[0]

    assert first_movie["alternativeName"] == test_data.get("api_search_1")


@allure.story("Тестирование строки поиска через API.")
@allure.title("Тест на поиск по кириллице.")
def test_search_by_cyrillic(base_url: str, api_key: str,
                            test_data: dict) -> None:
    api = SearchApi(base_url, api_key, test_data)
    resp = api.search_by_latin(test_data.get("api_search_2"))
    list_of_films = resp["docs"]
    first_movie = list_of_films[0]

    assert first_movie["name"] == test_data.get("api_search_2")


@allure.story("Тестирование строки поиска через API.")
@allure.title("Тест на поиск по цифрам.")
def test_search_by_numbers(base_url: str, api_key: str,
                           test_data: dict) -> None:
    api = SearchApi(base_url, api_key, test_data)
    resp = api.search_by_numbers(test_data.get("api_search_3"))
    list_of_films = resp["docs"]
    year_first_movie = list_of_films[0]

    assert str(year_first_movie["year"]) == test_data.get("api_search_3")


@allure.story("Тестирование строки поиска через API.")
@allure.title("Тест на поиск по произвольному набору букв.")
def test_search_by_arbitrary_set_of_letters(base_url: str, api_key: str,
                                            test_data: dict):
    api = SearchApi(base_url, api_key, test_data)
    resp = (api.search_by_arbitrary_set_of_letters
            (test_data.get("api_search_4")))
    list_of_films = resp["docs"]

    assert len(list_of_films) == 0


@allure.story("Тестирование строки поиска через API.")
@allure.title("Тест на поиск без токен.")
def test_search_without_an_apikey(base_url: str, api_key: str,
                                  test_data: dict):
    api = SearchApi(base_url, api_key, test_data)
    resp = api.search_without_an_apikey("api_search_5")
    message = resp.json()

    assert message["message"] == "В запросе не указан токен!"
    assert resp.status_code == 401
