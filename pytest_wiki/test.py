from pytest_wiki.wiki_page import WikiProgrammingLanguagesPage
from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize("popularity_expected", [
    10000000,
    15000000,
    50000000,
    100000000,
    500000000,
    1000000000,
    1500000000
])
def test_popularity(browser, popularity_expected):
    browser.get('https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites')

    page = WikiProgrammingLanguagesPage(browser)

    failed_rows = False

    for row in page.table_popular.rows:
        popularity_actual = page.get_popularity_number(row)
        if popularity_actual < popularity_expected:
            website = page.get_popularity_website_name(row)
            frontend = page.get_popularity_frontend(row)
            backend = page.get_popularity_backend(row)
            print(f'{website} (Frontend:{frontend}|Backend:{backend}) has {popularity_actual} unique visitors per '
                  f'month. (Expected more than {popularity_expected})\n')
            failed_rows = True

    assert failed_rows is False, "There was failed rows"
