import pytest
import time
from pages.simple_elements import SimpleElementsPage

def test(page,base_url_elements):
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)
    
    simple_elements.click_button()

    actual_label_text = simple_elements.find_lebel_text()
    expect_label_text = 'You clicked the button!'
    simple_elements.test_lebel_after_click(expect_label_text,actual_label_text)
    

def test_hover_event(page,base_url_elements):
    simple_elements = SimpleElementsPage(page)
    page.goto(base_url_elements)
    
    simple_elements.hover_event()

    actual_label_text = simple_elements.find_lebel_text()
    expect_label_text = 'Mouse over event occurred!'
    simple_elements.test_lebel_after_click(expect_label_text,actual_label_text)