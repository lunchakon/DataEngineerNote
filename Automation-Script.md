# Automation tools and How to use it

Playwright is a free and open-source library for automating web browsers across Chromium, WebKit, and Firefox. It offers a unified API for interacting with these browsers

### Playwright

    pip3 install playwright

    

### Here's a simple example to navigate to a website and take a screenshot:

    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True for invisible browser
        page = browser.new_page()
        page.goto("https://www.example.com")
        page.screenshot(path="screenshot.png")
        browser.close()

https://playwright.dev/python/docs/writing-tests
