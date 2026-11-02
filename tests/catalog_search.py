from playwright.sync_api import Page, expect
import time

'''def test_search_filters_defect_catalog_rows(page: Page) -> None:
    page.goto("https://lebyy.com/practice/catalog.html")

    expect(page.get_by_text("8 row(s)")).to_be_visible()
    catalog_rows = page.get_by_test_id("catalog-row")
    expect(catalog_rows).to_have_count(8)

    page.get_by_role("searchbox", name="Search by id or title").fill("checkout")

    expect(page.get_by_text("1 row(s)")).to_be_visible()
    visible_row = catalog_rows.filter(has_text="LAB-101")
    expect(visible_row).to_be_visible()
    expect(visible_row).to_contain_text("Checkout total off by one")'''


'''def test_open_defect_search(page:Page):
    page.goto("https://lebyy.com/practice/catalog.html")
    page.locator("#statusFilter").select_option("Open")
    time.sleep(1)

    rows = page.get_by_test_id("catalog-row")
    expect(rows).to_have_count(4)

    expect(rows.filter(has_text="Open")).to_have_count(4)'''


'''def test_sort(page:Page):
    page.goto("https://lebyy.com/practice/catalog.html")
    page.get_by_test_id("sort-title").click()
    page.locator("#statusFilter").select_option("Open")
    time.sleep(1)

    rows = page.get_by_test_id("catalog-row")
    expect(rows.nth(0)).to_contain_text("Auth locked message missing i18n")
    page.get_by_test_id("sort-title").click()
    expect(rows.nth(0)).to_contain_text("Upload rejects .CSV silently")'''


'''def test_delayed_message_appears_after_loading(page: Page) -> None:
    page.goto("https://lebyy.com/practice/sync.html")

    delayed_message = page.get_by_text("Data arrived after 2.5 seconds")
    loading_label = page.get_by_text("Working…")
    load_button = page.get_by_role("button", name="Load delayed message")

    expect(delayed_message).to_be_hidden()
    load_button.click()

    expect(loading_label).to_be_visible()
    expect(loading_label).to_be_hidden()
    expect(delayed_message).to_be_visible()
    expect(load_button).to_be_enabled()'''


'''def test_toast_notification_appears_and_dismisses(page: Page) -> None:
    page.goto("https://lebyy.com/practice/sync.html")
    page.get_by_role("button", name="Show toast").click()

    toast_text = page.locator(".lab-toast")
    expect(toast_text).to_be_visible()
    expect(toast_text).to_contain_text("Toast fired at")
    toast_host = page.get_by_test_id("toast-host")
    expect(toast_host).to_be_visible()

    expect(toast_text).to_be_hidden()'''

    

