from playwright.sync_api import Page,expect
import time

def test_bug_report_form(page:Page):
    page.goto("http://lebyy.com/practice/forms.html")
    page.get_by_placeholder('Enter reporter name').fill("Mariam P Shaji")
    page.locator("#severity").select_option("Medium")
    time.sleep(2)
    page.locator("#skills").select_option(["Appium","Playwright"])
    
    #page.locator("//input[@value='firefox']").click()
    page.get_by_label("Firefox").check()
    time.sleep(2)
    page.locator("//input[@value='yes']").check()
    page.locator("//input[@id='foundOn']").fill("2026-10-27")
    time.sleep(2)
    page.locator("#summary").fill("Unable to login to application")
    time.sleep(2)
    page.locator("//button[@data-testid='submit-bug']").click()