import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from configuration.ConfigProvider import ConfigProvider
from test_data.DataProvider import DataProvider


class MainPage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__url = ConfigProvider().get("ui", "base_url")
        self.__data = DataProvider()

    @allure.step("Открытие главной страницы.")
    def open(self):
        self.__driver.get(self.__url)

    @allure.step("Нажатие капчи.")
    def capcha(self):
        try:
            wait = WebDriverWait(self.__driver, 10)
            capcha = wait.until(EC.presence_of_element_located
                                ((By.CSS_SELECTOR, "#js-button")))
            capcha.click()
        except TimeoutException:
            pass

    @allure.step("Закрытие всплывающего окна.")
    def close_content(self):
        try:
            wait = WebDriverWait(self.__driver, 10)
            content = wait.until(EC.presence_of_element_located
                                 ((By.CSS_SELECTOR,
                                   'button[data-tid="CloseButton"]')))
            content.click()
        except TimeoutException:
            pass

    @allure.step("Ввод запроса на кириллице.")
    def search_in_cyrillic(self) -> str:
        wait = WebDriverWait(self.__driver, 10)
        search_field = (wait.until
                        (EC.presence_of_element_located
                         ((By.CSS_SELECTOR, 'input[name="kp_query"]'))))
        search_field.send_keys(self.__data.get("ui_search_1"))
        (self.__driver.find_element
         (By.CSS_SELECTOR, '.search-form-submit-button__icon').click())
        result = (self.__driver.find_element
                  (By.CSS_SELECTOR, '.search_results_topText>b').text)
        return result

    @allure.step("Ввод запроса на латинице.")
    def search_by_latin(self) -> str:
        wait = WebDriverWait(self.__driver, 10)
        search_field = wait.until(EC.presence_of_element_located
                                  ((By.CSS_SELECTOR,
                                    'input[name="kp_query"]')))
        search_field.send_keys(self.__data.get("ui_search_2"))
        (self.__driver.find_element
         (By.CSS_SELECTOR, '.search-form-submit-button__icon').click())
        result = (self.__driver.find_element
                  (By.CSS_SELECTOR, '.search_results_topText>b').text)
        return result

    @allure.step("Ввод запроса в верхнем регистре.")
    def uppercase_search(self) -> str:
        wait = WebDriverWait(self.__driver, 10)
        search_field = (wait.until
                        (EC.presence_of_element_located
                         ((By.CSS_SELECTOR, 'input[name="kp_query"]'))))
        search_field.send_keys(self.__data.get("ui_search_3"))
        (self.__driver.find_element
         (By.CSS_SELECTOR, '.search-form-submit-button__icon').click())
        result = (self.__driver.find_element
                  (By.CSS_SELECTOR, '.search_results_topText>b').text)
        return result

    @allure.step("Ввод запроса в нижнем регистре.")
    def lowercase_search(self) -> str:
        wait = WebDriverWait(self.__driver, 10)
        search_field = (wait.until
                        (EC.presence_of_element_located
                         ((By.CSS_SELECTOR, 'input[name="kp_query"]'))))
        search_field.send_keys(self.__data.get("ui_search_4"))
        (self.__driver.find_element
         (By.CSS_SELECTOR, '.search-form-submit-button__icon').click())
        result = (self.__driver.find_element
                  (By.CSS_SELECTOR, '.search_results_topText>b').text)
        return result

    @allure.step("Ввод запроса со знаками препинания.")
    def search_with_punctuation(self, search_query) -> str:
        wait = WebDriverWait(self.__driver, 10)
        search_field = (wait.until
                        (EC.presence_of_element_located
                         ((By.CSS_SELECTOR, 'input[name="kp_query"]'))))
        search_field.send_keys(self.__data.get(search_query))
        (self.__driver.find_element
         (By.CSS_SELECTOR, '.search-form-submit-button__icon').click())
        result = (self.__driver.find_element
                  (By.CSS_SELECTOR, "span[data-tid='eb6be89']").text)
        return result
