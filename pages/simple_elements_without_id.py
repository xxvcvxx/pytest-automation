from playwright.sync_api import Page

class SimpleElementsPageWithoutid:
    
    def __init__(self, page:Page):
        self.page=page
        self.button_locator=".my-button" #Xpath - //button[@class='my-button']
        self.results_locator="#results-container"
        self.hover_event_locator="label[onmouseover='labelOnMouseOver()']" #Xpath - //label[@onmouseover='labelOnMouseOver()']
        self.input_locator=".my-input[type='text']" #xpath - self.input_locator = "//input[@class='my-input' and @type='text']"

        
    def click_button(self):
        self.page.locator(self.button_locator).click()
        
    def hover_event(self):
        self.page.locator(self.hover_event_locator).hover()
    
    def input_field_value_change(self,text):
        self.page.locator(self.input_locator).fill(text)
        self.page.locator("body").click()
        
     # Assert
        
    def test_result_text(self,expect_text):
        locator=self.page.locator(self.results_locator)
        locator.wait_for(state="visible",timeout=5000)
        actual_text = locator.text_content()
        assert actual_text == expect_text, f"Expected '{expect_text}', but got '{actual_text}'"