from playwright.sync_api import Page, expect

import time
from playwright.sync_api import BrowserContext

'''def test_frame_locator(page:Page):
    page.goto("https://lebyy.com/practice/frames.html")

    frame = page.frame_locator('[data-testid = "lab-iframe"]')

    expect(frame.get_by_test_id("frame-heading")).to_have_text("Inside the iframe")

    expect(frame.locator("#frameStatus")).to_have_text("Waiting…")

    frame.locator("#frameBtn").click()

    expect(frame.locator("#frameStatus")).to_have_text("Frame action completed")'''



'''def test_nested_frame(page:Page):
    page.goto("https://lebyy.com/practice/frames.html")

    child = page.frame_locator('[data-testid = "frame-nested-parent"]').frame_locator(
        '[data-testid = "frame-nested-child"]'
    )


    child.get_by_test_id("nested-child-input").fill("mariam")
    time.sleep(2)
    child.get_by_test_id("nested-child-btn").click()
    expect(child.locator("#cStatus")).to_have_text("Saved: mariam")'''


'''def test_helper_tab_opens_with_correct_title(
    page: Page, context: BrowserContext
) -> None:
    page.goto("https://lebyy.com/practice/frames.html")

    with context.expect_page() as helper_page_info:
        page.get_by_role("button", name="Open helper tab").click()

    helper_page = helper_page_info.value
    helper_page.wait_for_load_state()

    expect(helper_page).to_have_title("Lebyy Lab Helper")
    expect(helper_page.get_by_role("heading", name="Lebyy Lab Helper")).to_be_visible()
    expect(helper_page.locator("body")).to_contain_text("multi-tab automation practice")
    expect(page.get_by_text("Helper tab opened")).to_be_visible()

    helper_page.close()'''



