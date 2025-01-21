import pytest
from pages.elements_disabled import ElementsDisabled

@pytest.fixture
def elements_disabled(page, base_url_element_disabled):
    elements_disabled = ElementsDisabled(page)
    page.goto(base_url_element_disabled)
    return elements_disabled
    
def test_url(elements_disabled):
    # Assert
    elements_disabled.verify_url()

def test_button_disabled(elements_disabled):
    # Assert
    elements_disabled.verify_element_is_disabled()
    
def test_button_enabled(elements_disabled):
    # Assert
    elements_disabled.verify_element_is_enabled()