from playwright.sync_api import sync_playwright

def quote():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()

        page.goto("https://www.squareone.ca/")

        page.wait_for_selector("input[placeholder='Enter your home address']", timeout=5000)

        page.locator("input[placeholder='Enter your home address']").first.fill("123 Main St, Vancouver, BC")

        page.wait_for_selector("button[data-quote-product-type='HOME']", timeout=5000)
        page.locator("button[data-quote-product-type='HOME']").click()

        page.locator("button:has-text('I am the owner of the home')").scroll_into_view_if_needed()

        page.wait_for_selector("text=I am the owner of the home", timeout=5000)

        page.locator("div:has-text('Do you own the home or rent it?') input[type='radio']").nth(0).check()

        page.locator("label:has-text('I am the owner of the home')").click()


        page.locator("div:has-text('Detached house')").click()

        assert page.locator("div:has-text('Detached house')").is_checked(), "Selection failed"

        page.pause()
        browser.close()

quote()

