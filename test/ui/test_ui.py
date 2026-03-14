import allure
import pytest
from pages.MainPage import MainPage


@pytest.mark.ui
@allure.story("Тестирование строки поиска.")
@allure.title("Тест на поиск по кириллице.")
def test_search_by_cyrillic(browser, test_data: dict):
    main_page = MainPage(browser)
    main_page.open()
    main_page.capcha()
    main_page.close_content()
    result = main_page.search_in_cyrillic()
    assert result == test_data.get("ui_search_1")


@pytest.mark.ui
@allure.story("Тестирование строки поиска.")
@allure.title("Тест на поиск по латинице.")
def test_search_by_latin(browser, test_data: dict):
    main_page = MainPage(browser)
    main_page.open()
    main_page.capcha()
    main_page.close_content()
    result = main_page.search_by_latin()
    assert result == test_data.get("ui_search_2")


@pytest.mark.ui
@allure.story("Тестирование строки поиска.")
@allure.title("Тест на поиск с верхним регистром.")
def test_uppercase_search(browser, test_data: dict):
    main_page = MainPage(browser)
    main_page.open()
    main_page.capcha()
    main_page.close_content()
    result = main_page.uppercase_search()
    assert result == test_data.get("ui_search_3")


@pytest.mark.ui
@allure.story("Тестирование строки поиска.")
@allure.title("Тест на поиск с нижним регистром.")
def test_lowercase_search(browser, test_data: dict):
    main_page = MainPage(browser)
    main_page.open()
    main_page.capcha()
    main_page.close_content()
    result = main_page.lowercase_search()
    assert result == test_data.get("ui_search_4")


@pytest.mark.ui
@allure.story("Тестирование строки поиска.")
@allure.title("Тест на поиск со знаками препинания.")
def test_search_with_punctuation(browser, test_data: dict):
    main_page = MainPage(browser)
    main_page.open()
    main_page.capcha()
    main_page.close_content()
    result = main_page.search_with_punctuation("ui_search_5")
    assert result == test_data.get("ui_search_5")
