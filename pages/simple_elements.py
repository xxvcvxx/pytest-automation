from playwright.sync_api import Page

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
    
    
    #Assert

    def test_result_text(self,actual_text,expect_text):
        assert actual_text == expect_text, f"Expected '{expect_text}', but got '{actual_text}'"
    
    def test_label_text(selfself,actual_text,expect_text): # Assert method specific to label element for better clarity.
        assert  actual_text == expect_text, f"Expected '{expect_text}', but got '{actual_text}'"