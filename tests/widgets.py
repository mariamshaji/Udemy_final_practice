from playwright.sync_api import Page,expect
import time


'''def test_widget_search(page:Page):
    page.set_default_navigation_timeout(50000)
    page.goto("https://lebyy.com/practice/widgets.html",wait_until="domcontentloaded")
    search_word = page.get_by_test_id("autosuggest-input")
    search_word.fill("pla")

    suggestion = page.get_by_text("Playwright",exact=True)
    expect(suggestion).to_be_visible()

    suggestion.click()

    expect(page.locator("#suggestPicked")).to_have_text("Selected: Playwright")
    #expect(page.get_by_text("Selected: Playwright")).to_be_visible()'''

'''def test_widget_calendar(page:Page):
    page.set_default_navigation_timeout(50000)
    page.goto("https://lebyy.com/practice/widgets.html",wait_until="domcontentloaded")
    page.locator("#calInput").click()
    page.locator("#calNext").click()
    page.get_by_test_id("calendar-day-18").click()
    date = page.locator("#calInput").input_value()
    expect(page.locator("#calPicked")).to_have_text(f"Selected: {date}")
    
    time.sleep(2)'''

def test_widget_action(page:Page):
    page.set_default_navigation_timeout(50000)
    page.goto("https://lebyy.com/practice/widgets.html",wait_until="domcontentloaded")
    page.locator("#ddToggle").click()
    action = page.get_by_test_id("dd-item-another")
    selected_action = action.inner_text()
    action.click()
    
    expect(page.locator("#ddResult")).to_have_text(f"Chosen: {selected_action}")


