import pytest
import time
from pages.simple_elements import SimpleElementsPage

def test_click_event(page, base_url_elements):
    # Arrange
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)
    
    # Act
    simple_elements.click_button()

    # Assert
    expect_result_text = 'You clicked the button!'
    simple_elements.test_result_text(expect_result_text)

def test_hover_event(page, base_url_elements):
    # Arrange
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)
    
    # Act
    simple_elements.hover_event()

    # Assert
    expect_result_text = 'Mouse over event occurred!'
    simple_elements.test_result_text(expect_result_text)

def test_label_text(page, base_url_elements):
    # Arrange
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)

    # Assert
    expect_result_text = 'Some text for label'
    simple_elements.test_label_text(expect_result_text)

@pytest.mark.parametrize("click_times, expect_result_text",[
    (1,'Checkbox is checked!'),
    (2,'Checkbox is unchecked!'),
])

def test_checkbox_checked_text(page, base_url_elements,click_times,expect_result_text):
     # Arrange
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)

    # Act
    for _ in range(click_times):
        simple_elements.click_checkbox()

    
    # Assert
    simple_elements.test_result_text(expect_result_text)
    
def test_textarea(page,base_url_elements):
    # Arrange
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)
    
    # Act
    sample_text = "text in textarea"
    simple_elements.fill_textarea(sample_text)
    
    # Assert
    expect_result_text = f"Textarea value changed to: {sample_text}"
    simple_elements.test_result_text(expect_result_text)
    
def test_input(page,base_url_elements):
    # Arrange
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)
    
    # Act
    sample_text = "text in input"
    simple_elements.fill_input(sample_text)
    
    # Assert
    expect_result_text = f"Input value changed to: {sample_text}"
    simple_elements.test_result_text(expect_result_text)
    
@pytest.mark.parametrize("option_value, expect_result_text", [
    ("option1", "Selected option: option1"),
    ("option2", "Selected option: option2"),
    ("option3", "Selected option: option3"),
])

def test_dropdown(page,base_url_elements,option_value,expect_result_text):
    # Arrange
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)
    
    # Act
    simple_elements.select_option(option_value)
    
    # Assert
    simple_elements.test_result_text(expect_result_text)
    
@pytest.mark.parametrize("button_id, expect_result_text", [
    ("1", "Radio Button 1 clicked!"),
    ("2", "Radio Button 2 clicked!"),
    ("3", "Radio Button 3 clicked!"),
])

def test_radio_buttons(page,base_url_elements,button_id,expect_result_text):
    # Arrange
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)
    
    #Act
    simple_elements.select_radio_button(button_id)
    
    # Assert
    simple_elements.test_result_text(expect_result_text)
    
