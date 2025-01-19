import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 'headless=False' - visible browser
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def base_url_elements():
    return "http://localhost:3000/practice/simple-elements.html"

def base_url_element_without_id():
    return ""

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
