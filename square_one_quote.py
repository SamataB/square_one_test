from playwright.sync_api import sync_playwright

def complete_quote():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()

        page.goto("https://www.squareone.ca")

        page.get_by_role("button", name="Get a quote").click()

        page.locator("text=I own the home").click()

        page.locator('//*[@id="sq1-qw-bf25f3a43f39_locationAddress_address"]').fill("123 Main St, Vancouver, BC")

        page.get_by_role("button", name="Continue").click()

        page.screenshot(path="quote_submission.png")

        browser.close()

# Run the function
complete_quote()
