import pytest
import time
from pages.simple_elements import SimpleElementsPage

def test_click_event(page, base_url_elements):
    # Arrange
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)
    
    # Act
    simple_elements.click_button()
    actual_result_text = simple_elements.find_result_text()

    # Assert
    expect_result_text = 'You clicked the button!'
    simple_elements.test_result_text(expect_result_text, actual_result_text)

def test_hover_event(page, base_url_elements):
    # Arrange
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)
    
    # Act
    simple_elements.hover_event()
    actual_result_text = simple_elements.find_result_text()

    # Assert
    expect_result_text = 'Mouse over event occurred!'
    simple_elements.test_result_text(expect_result_text, actual_result_text)

def test_label_text(page, base_url_elements):
    # Arrange
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)

    # Act
    actual_result_text = simple_elements.find_label_text()

    # Assert
    expect_result_text = 'Some text for label'
    simple_elements.test_result_text(expect_result_text, actual_result_text)

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
    actual_result_text = simple_elements.find_result_text()
    
    # Assert
    simple_elements.test_result_text(expect_result_text, actual_result_text)
    
def test_textarea(page,base_url_elements):
    # Arrange
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)
    
    # Act
    sample_text = "text in textarea"
    simple_elements.fill_textarea(sample_text)
    actual_result_text = simple_elements.find_result_text()
    
    # Assert
    expect_result_text = f"Textarea value changed to: {sample_text}"
    simple_elements.test_result_text(expect_result_text, actual_result_text)
    
def test_input(page,base_url_elements):
    # Arrange
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)
    
    # Act
    sample_text = "text in input"
    simple_elements.fill_input(sample_text)
    actual_result_text = simple_elements.find_result_text()
    
    # Assert
    expect_result_text = f"Input value changed to: {sample_text}"
    simple_elements.test_result_text(expect_result_text, actual_result_text)
    
    
