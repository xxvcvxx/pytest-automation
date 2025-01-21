from playwright.sync_api import Page, expect

class ElementsDisabled:
    
    def __init__(self, page:Page):
        self.page=page
        self.button_locator="#id-button-element"
        self.results_locator="#results"
        self.delay_label_locator="#delayLabel"
        
    def click_button(self):
        self.page.locator(self.button_locator).click()
    
    def delay_time(self):
        delay = self.page.locator(self.delay_label_locator).text_content() 
        delay_seconds = float(delay)  
        return int((delay_seconds * 1000)+1000)
           
     # Assert
     
    def test_result_text(self,expect_text):
        locator=self.page.locator(self.results_locator)
        locator.wait_for(state="visible",timeout=5000)
        actual_text = locator.text_content()
        assert actual_text == expect_text, f"Expected '{expect_text}', but got '{actual_text}'"
        
    def verify_url(self):
        expect(self.page).to_have_url("http://localhost:3000/practice/disabled-elements-1.html")
        
    def verify_element_is_disabled(self):
        expect(self.page.locator(self.button_locator)).to_be_disabled()
        
    def verify_element_is_enabled(self):
        timeout = self.delay_time()
        locator = self.page.locator(self.button_locator)
        expect(locator).to_be_enabled(timeout=timeout)