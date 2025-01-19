import pytest
from pages.simple_elements_without_id import SimpleElementsPageWithoutid

def test_click_event(page, base_url_elements):
    # Arrange
    simple_elements_without_id = SimpleElementsPageWithoutid(page)
    page.goto(base_url_elements)
    
    # Act
    simple_elements_without_id.click_button()

    # Assert
    expect_result_text = 'You clicked the button!'
    simple_elements_without_id.test_result_text(expect_result_text)

