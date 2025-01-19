from playwright.sync_api import Page

class SimpleElementsPageWithoutid:
    
    def __init__(self, page:Page):
        self.page=page
        self.button_locator=".my-button" #Xpath - //button[@class='my-button']
        self.results_locator="#results-container"
        
    def click_button(self):
        self.page.locator(self.button_locator).click()
        
     # Assert
        
    def test_result_text(self,expect_text):
        locator=self.page.locator(self.results_locator)
        locator.wait_for(state="visible",timeout=5000)
        actual_text = locator.text_content()
        assert actual_text == expect_text, f"Expected '{expect_text}', but got '{actual_text}'"