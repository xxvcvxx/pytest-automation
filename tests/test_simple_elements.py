import pytest
from pages.simple_elements import SimpleElementsPage

@pytest.fixture
def simple_elements(page, base_url_elements):
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)
    return simple_elements

def test_click_event(simple_elements):
    # Act
    simple_elements.click_button()

    # Assert
    expect_result_text = 'You clicked the button!'
    simple_elements.test_result_text(expect_result_text)

def test_hover_event(simple_elements):
    # Act
    simple_elements.hover_event()

    # Assert
    expect_result_text = 'Mouse over event occurred!'
    simple_elements.test_result_text(expect_result_text)

def test_label_text(simple_elements):
    # Assert
    expect_result_text = 'Some text for label'
    simple_elements.test_label_text(expect_result_text)

@pytest.mark.parametrize("click_times, expect_result_text",[ 
    (1,'Checkbox is checked!'),
    (2,'Checkbox is unchecked!'),
])
def test_checkbox_checked_text(simple_elements, click_times, expect_result_text):
    # Act
    for _ in range(click_times):
        simple_elements.click_checkbox()

    # Assert
    simple_elements.test_result_text(expect_result_text)
    
def test_textarea(simple_elements):
    # Act
    sample_text = "text in textarea"
    simple_elements.fill_textarea(sample_text)
    
    # Assert
    expect_result_text = f"Textarea value changed to: {sample_text}"
    simple_elements.test_result_text(expect_result_text)
    
def test_input(simple_elements):
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
def test_dropdown(simple_elements, option_value, expect_result_text):
    # Act
    simple_elements.select_option(option_value)
    
    # Assert
    simple_elements.test_result_text(expect_result_text)
    
@pytest.mark.parametrize("button_id, expect_result_text", [
    ("1", "Radio Button 1 clicked!"),
    ("2", "Radio Button 2 clicked!"),
    ("3", "Radio Button 3 clicked!"),
])
def test_radio_buttons(simple_elements, button_id, expect_result_text):
    # Act
    simple_elements.select_radio_button(button_id)
    
    # Assert
    simple_elements.test_result_text(expect_result_text)
    
@pytest.mark.parametrize("value",[100,50,0])
def test_slider_range(simple_elements, value):
    # Act
    simple_elements.range_slider_onchange_event(str(value))
    
    # Assert
    expect_result_text = f'Range value changed to: {value}'
    simple_elements.test_result_text(expect_result_text)
    
def test_date_picker(simple_elements): 
    # Act
    expect_result_text = f"Selected date: {simple_elements.date_picker()}"

    # Assert
    simple_elements.test_result_text(expect_result_text)

def test_color_picker(simple_elements):
    # Act
    color_value = "#00ff00"  # Green
    simple_elements.color_picker(color_value)
    rgb_value = simple_elements.hexToRgb(color_value)

    # Assert
    expect_result_text = f"New selected color: {color_value} as hex and in RGB: {rgb_value}"
    simple_elements.test_result_text(expect_result_text)

@pytest.mark.parametrize("hex_color,expected_rgb", [
    ("#ff0000", "rgb(255, 0, 0)"),
    ("#00ff00", "rgb(0, 255, 0)"),
    ("#0000ff", "rgb(0, 0, 255)"),
    ("#ffffff", "rgb(255, 255, 255)"),
    ("#000000", "rgb(0, 0, 0)"),
    ("#ffa500", "rgb(255, 165, 0)"),  
    ("#800080", "rgb(128, 0, 128)"),  
])
def test_color_picker_with_parameters(simple_elements, hex_color, expected_rgb):
    # Act
    simple_elements.color_picker(hex_color)

    # Assert
    expect_result_text = f"New selected color: {hex_color} as hex and in RGB: {expected_rgb}"
    simple_elements.test_result_text(expect_result_text)
    
def test_checkbox_toggle_and_check(simple_elements):
    # Act
    simple_elements.click_checkbox()
    
    # Asset
    simple_elements.test_checkbox_is_checked()
