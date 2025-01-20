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

@pytest.mark.parametrize("button_id, expect_result_text", [
    ("1", "Radio Button 1 clicked!"),
    ("2", "Radio Button 2 clicked!"),
    ("3", "Radio Button 3 clicked!"),
])
    
def test_radio_buttons(simple_elements_without_id, button_id, expect_result_text):

    #Act
    simple_elements_without_id.select_radio_button(button_id)
    
    #Assert
    simple_elements_without_id.test_result_text(expect_result_text)
    
@pytest.mark.parametrize("click_times, expect_result_text",[ 
    (1,'Checkbox is checked!'),
    (2,'Checkbox is unchecked!'),
])
    
def test_checkbox(simple_elements_without_id, click_times, expect_result_text):
    
    #Act 
    for _ in range (click_times):
        simple_elements_without_id.click_checkbox()
        
    #Assert
    simple_elements_without_id.test_result_text(expect_result_text)
    