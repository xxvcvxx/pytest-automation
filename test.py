from playwright.sync_api import sync_playwright

# Start Playwright with Chromium
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Set to False to see the browser
    page = browser.new_page()
    page.goto('https://example.com')  # Open a website
    print(page.title())  # Print the title of the page
    browser.close()
