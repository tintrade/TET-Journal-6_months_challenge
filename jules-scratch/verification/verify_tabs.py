from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Get the absolute path to the HTML file
    file_path = os.path.abspath("index.html")
    # Construct the file URL
    file_url = f"file://{file_path}"

    # Navigate to the local file
    page.goto(file_url)

    # Click on the "Review Notes" tab
    page.click('button[data-tab="review-notes-tab"]')
    page.wait_for_timeout(500) # Wait for animation
    page.screenshot(path="jules-scratch/verification/verification_review_notes.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)