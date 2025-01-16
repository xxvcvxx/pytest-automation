from playwright.sync_api import Page
from datetime import datetime, timedelta

class SimpleElementsPage:
    def __init__(self, page:Page):
        self.page=page
        self.label_text_locator="#id-label-element"
        self.button_locator="#id-button-element"
        self.results_locator="#results"
        self.hover_event_locator="#id-tooltip-element"
        self.checkbox_locator="#id-checkbox"
        self.input_locator="#id-input"
        self.textarea_locator="#id-textarea"
        self.dropdown_locator="#id-dropdown"
        self.radiobutton_locator="#id-radio"
        self.slider_locator="#id-range"
        self.date_picker_locator="#id-date"
        self.color_picker_locator="#id-color"

    def click_button(self):
        self.page.locator(self.button_locator).click()

    def hover_event(self):
        self.page.locator(self.hover_event_locator).hover()
        
    def click_checkbox(self):
        self.page.locator(self.checkbox_locator).click()
        
    def fill_input(self,text):
        self.page.locator(self.input_locator).fill(text)
        self.page.locator("body").click()
        
    def fill_textarea(self,text):
        self.page.locator(self.textarea_locator).fill(text)
        self.page.locator("body").click()

    def find_result_text(self):
        locator=self.page.locator(self.results_locator)
        locator.wait_for(state="visible",timeout=5000)
        return locator.text_content()
    
    def find_label_text(self):
        locator=self.page.locator(self.label_text_locator)
        locator.wait_for(state="visible",timeout=5000)
        return locator.text_content()
    
    def select_option(self, value: str):
        locator=self.page.locator(self.dropdown_locator)
        locator.select_option(value)
        
    def select_radio_button(self,value):
        full_locator=f"{self.radiobutton_locator}{value}"
        self.page.locator(full_locator).click()
        
    def range_slider_onchange_event(self,value):
        locator=self.page.locator(self.slider_locator)
        locator.fill(value)
        
    def date_picker(self):
        locator=self.page.locator(self.date_picker_locator)
        locator.evaluate("document.querySelector('#id-date').showPicker()")
        self.page.keyboard.press("ArrowRight")
        self.page.keyboard.press("Enter")
        return (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    
    def color_picker(self,color_value):
        self.page.locator(self.color_picker_locator).fill(color_value)
    
    def hexToRgb(self,hex):
        # Usuń znak # jeśli jest
        hex = hex.lstrip('#')
        
        # Przekształć wartości hex na RGB
        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)
        
        return f"rgb({r}, {g}, {b})"
        
    #Assert

    def test_result_text(self,expect_text):
        actual_text = self.find_result_text()
        assert actual_text == expect_text, f"Expected '{expect_text}', but got '{actual_text}'"
    
    def test_label_text(self,expect_text): # Assert method specific to label element for better clarity.
        actual_text = self.find_label_text()
        assert  actual_text == expect_text, f"Expected '{expect_text}', but got '{actual_text}'"