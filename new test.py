from playwright.sync_api import sync_playwright

def quote():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)  # Slow down for better visibility
        page = browser.new_page()

        page.goto("https://www.squareone.ca/")

        page.wait_for_selector("input[placeholder='Enter your home address']", timeout=5000)
        page.locator("input[placeholder='Enter your home address']").first.fill("123 Main St, Vancouver, BC")

        page.wait_for_selector("button[data-quote-product-type='HOME']", timeout=5000)
        page.locator("button[data-quote-product-type='HOME']").click()

        page.wait_for_load_state("networkidle")

        owner_radio_button = page.locator("label:has-text('I am the owner of the home')")

        owner_radio_button.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)  # Small delay to allow for smooth scrolling

        owner_radio_button.click(force=True)
        print(page.locator("label:has-text('I am the owner of the home')").count())

        page.pause()

        browser.close()

# Call the function
quote()
