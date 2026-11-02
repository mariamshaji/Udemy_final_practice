from playwright.sync_api import Page,expect
import time
import re


'''def test_hover(page:Page):
    page.set_default_navigation_timeout(50000)
    page.goto("https://lebyy.com/practice/interactions.html",wait_until="domcontentloaded")
    page.get_by_test_id("hover-trigger").hover()
    page.get_by_role("button",name="Open docs").click()
    expect(page.locator("#hoverResult")).to_have_text("Selected: Open docs")'''


'''def test_double_click(page:Page):
    page.set_default_navigation_timeout(50000)
    page.goto("https://lebyy.com/practice/interactions.html",wait_until="domcontentloaded")
    page.locator("#dblTarget").dblclick()
    expect(page.locator("#dblResult")).to_have_text("Double-click registered")'''


'''def test_righ_click(page:Page):
    page.set_default_navigation_timeout(50000)
    page.goto("https://lebyy.com/practice/interactions.html",wait_until="domcontentloaded")
    page.locator("#contextTarget").click(button="right")
    page.get_by_test_id("ctx-copy").click()
    expect(page.locator("#contextResult")).to_have_text("Context action: copy")
    time.sleep(2)'''


'''def test_drag_drop(page:Page):
    page.set_default_navigation_timeout(50000)
    page.goto("https://lebyy.com/practice/interactions.html",wait_until="domcontentloaded")
    source = page.locator("#task-cart")
    target = page.locator("#done")
    source.drag_to(target)
    time.sleep(2) '''

def test_alert_dialog(page:Page):
    page.set_default_navigation_timeout(50000)
    page.goto("https://lebyy.com/practice/dialogs.html",wait_until="domcontentloaded")

    #alert
    def handle_dialog(dialog):
            print(dialog.message)
            assert dialog.type == 'confirm'
            dialog.dismiss()


    '''page.on("dialog",handle_dialog)
    page.locator("#btnAlert").click()'''

    #showing message
    '''page.on("dialog",lambda dialog:dialog.accept("mariam"))
    page.locator("#btnPrompt").click()'''

    #dismiss
    page.on("dialog",handle_dialog)
    page.locator("#btnConfirm").click()

    


   
    time.sleep(2)   



