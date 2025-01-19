import pytest
from pages.simple_elements_without_id import SimpleElementsPageWithoutid

@pytest.fixture
def simple_elements_without_id(page, base_url_element_without_id):
    simple_elements_without_id = SimpleElementsPageWithoutid(page)
    page.goto(base_url_element_without_id)
    return simple_elements_without_id

def test_click_event(simple_elements_without_id):

    # Act
    simple_elements_without_id.click_button()

    # Assert
    expect_result_text = 'You clicked the button!'
    simple_elements_without_id.test_result_text(expect_result_text)
    
def test_hover_event(simple_elements_without_id):
    # Act
    simple_elements_without_id.hover_event()

    # Assert
    expect_result_text = 'Mouse over event occurred!'
    simple_elements_without_id.test_result_text(expect_result_text)
    
def test_input_field_value_change(simple_elements_without_id):
    #Act
    text = "AAA"
    simple_elements_without_id.input_field_value_change(text)
    
    #Assert
    simple_elements_without_id.test_result_text("Input value changed to: AAA")

