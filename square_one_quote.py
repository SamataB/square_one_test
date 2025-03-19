from playwright.sync_api import sync_playwright

def complete_quote():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)  # Set headless=True to run without UI
        page = browser.new_page()

        # Step 1: Visit Square One website
        page.goto("https://www.squareone.ca")

        # Step 2: Click "Get a quote" (Assuming there's a button with this text)
        page.get_by_role("button", name="Get a quote").click()

        # Step 3: Select "I own the home" (Modify if the actual selector is different)
        page.locator("text=I own the home").click()

        # Step 4: Fill out form fields (Example selectors, adjust as needed)
         # Fill the address field
        page.locator('//*[@id="sq1-qw-bf25f3a43f39_locationAddress_address"]').fill("123 Main St, Vancouver, BC")

        # Step 5: Click "Next" or "Continue"
        page.get_by_role("button", name="Continue").click()

        # Step 6: Additional form steps (modify according to the actual process)
        # e.g., filling property details, selecting coverage, etc.

        # Step 7: Capture screenshot for verification
        page.screenshot(path="quote_submission.png")

        browser.close()

# Run the function
complete_quote()
