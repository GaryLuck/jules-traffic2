from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    page.goto("http://localhost:8000/index.html")
    page.wait_for_timeout(500)

    # Move entry rate slider
    page.get_by_label("Entry Rate (Cars/tick)").fill("0.8")
    page.wait_for_timeout(500)

    # Move initial speed slider
    page.get_by_label("Initial Speed of Arriving Cars").fill("5")
    page.wait_for_timeout(500)

    # Click restart to see changes
    page.get_by_role("button", name="Restart & Create Jam").click()
    page.wait_for_timeout(1000)

    # Take screenshot at the key moment
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)  # Hold final state for the video

if __name__ == "__main__":
    os.makedirs("/home/jules/verification/videos", exist_ok=True)
    os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()  # MUST close context to save the video
            browser.close()
