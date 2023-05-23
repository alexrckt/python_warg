from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from pytest_wiki.table import Table, parse_numeric_data


class WikiProgrammingLanguagesPage:
    TABLE_POPULAR = (By.XPATH, "//caption[contains(text(),'Programming languages used in most popular websites*')]/..")

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)
        self.table_popular = Table(table_element=self.driver.find_element(*self.TABLE_POPULAR))

    def get_popularity_number(self, row):
        data = self.table_popular.get_row_data_by_column_name(row, "Popularity(unique visitors per month)")
        return parse_numeric_data(data)

    def get_popularity_website_name(self, row):
        return self.table_popular.get_row_data_by_column_name(row, "Websites")

    def get_popularity_frontend(self, row):
        return self.table_popular.get_row_data_by_column_name(row, "Front-end(Client-side)")

    def get_popularity_backend(self, row):
        return self.table_popular.get_row_data_by_column_name(row, "Back-end(Server-side)")