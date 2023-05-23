import re
from dataclasses import dataclass
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def _removing_wiki_brackets(string):
    return re.sub(r"\[.*?]", "", string)


def _removing_clarifications(string):
    return re.sub(r"\(.*?\)", "", string)


def _removing_pointers(string):
    return re.sub(r"[.,]", "", string)


def _removing_tabs(string):
    return re.sub(r"\n", "", string)


def parse_numeric_data(string):
    return int(_removing_pointers(_removing_clarifications(string)).replace(" ", ""))


@dataclass
class Table:
    table_element: WebElement
    headers: List[str] = List[str]
    rows: List[List[str]] = List[List[str]]

    def __post_init__(self):
        self._parse_table()

    TABLE_HEADERS = (By.XPATH, "./thead/tr/th")
    TABLE_ROWS = (By.XPATH, "./tbody/tr")
    ROWS_DATA = (By.XPATH, "./td")

    def _parse_table(self):
        headers_elements = self.table_element.find_elements(*self.TABLE_HEADERS)
        self.headers = [_removing_tabs(_removing_wiki_brackets(element.text)) for element in headers_elements]

        rows_elements = self.table_element.find_elements(*self.TABLE_ROWS)
        self.rows = []
        for row_element in rows_elements:
            row_data_elements = row_element.find_elements(*self.ROWS_DATA)
            row = [_removing_wiki_brackets(element.text) for element in row_data_elements]
            self.rows.append(row)

    def get_row_data_by_column_name(self, row, column_name):
        column_number = self.headers.index(column_name)
        return row[column_number]
