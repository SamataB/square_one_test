from playwright.sync_api import sync_playwright

def quote():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()

        # Open Square One website
        page.goto("https://www.squareone.ca/")

       # Wait for the address field to be visible
        page.wait_for_selector("input[placeholder='Enter your home address']", timeout=5000)

        # Fill the address field (ensuring it's the first matching element)
        page.locator("input[placeholder='Enter your home address']").first.fill("123 Main St, Vancouver, BC")

        page.wait_for_selector("button[data-quote-product-type='HOME']", timeout=5000)
        # Click the "Home Quote" button
        page.locator("button[data-quote-product-type='HOME']").click()

        #scroll to view
         # ✅ Scroll into view before clicking (Fixed issue)
        page.locator("button:has-text('I am the owner of the home')").scroll_into_view_if_needed()

        # ✅ Wait for radio button to be visible before clicking
        page.wait_for_selector("text=I am the owner of the home", timeout=5000)

        # ✅ Select "I am the owner of the home"
        page.locator("text=I am the owner of the home").click()

        page.pause()
        browser.close()

# Call the function
quote()

