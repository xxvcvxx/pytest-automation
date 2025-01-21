import pytest
from pages.simple_elements import SimpleElementsPage
from playwright.sync_api import sync_playwright
from pages.simple_elements_without_id import SimpleElementsPageWithoutid

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 'headless=False' - visible browser
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:3000/practice"

@pytest.fixture(scope="session")
def base_url_elements(base_url):
    return f"{base_url}/simple-elements.html"

@pytest.fixture(scope="session")
def base_url_element_without_id(base_url):
    return f"{base_url}/simple-elements-no-ids.html"

@pytest.fixture(scope="session")
def base_url_element_disabled(base_url):
    return f"{base_url}/disabled-elements-1.html"

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


