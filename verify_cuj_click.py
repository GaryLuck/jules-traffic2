from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    page.goto("http://localhost:8000/index.html")
    page.wait_for_timeout(500)

    # Slow down simulation to make it easier to see cars added
    page.get_by_label("Simulation Speed").fill("1000")
    page.wait_for_timeout(500)

    # Click on the canvas to add cars
    canvas = page.locator("#roadCanvas")
    box = canvas.bounding_box()

    # Click empty spaces. The road has 50 cells, canvas width is 900.
    # Each cell is 18px wide.
    # We will click near the left side, middle, and right side.

    # 1. Click around x=20 (cell 1)
    page.mouse.click(box["x"] + 20, box["y"] + 20)
    page.wait_for_timeout(500)

    # 2. Click around x=100 (cell 5)
    page.mouse.click(box["x"] + 100, box["y"] + 20)
    page.wait_for_timeout(500)

    # 3. Click around x=800 (cell 44)
    page.mouse.click(box["x"] + 800, box["y"] + 20)
    page.wait_for_timeout(500)

    # Take screenshot at the key moment
    page.screenshot(path="/home/jules/verification/screenshots/verification2.png")
    page.wait_for_timeout(2000)  # Hold final state for the video

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
