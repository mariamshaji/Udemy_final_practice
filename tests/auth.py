from playwright.sync_api import Page,expect
import time,re


def test_auth_valid(page:Page):
    page.goto("https://lebyy.com/practice/auth.html",wait_until="domcontentloaded")
    username = "qa_learner"
    page.locator("#username").fill(username)
    
    page.locator("#password").fill("Lebyy@Lab1")
    page.get_by_role("button",name="Sign in").click()
    time.sleep(1)
    expect(page).to_have_url(re.compile(r"dashboard\.html"))
    expect(page.locator("h1")).to_have_text("Welcome to your lab session")
    expect(page.locator(".lab-lead")).to_contain_text("signed in")
    expect(page.locator("#sessionUser")).to_contain_text(username)


def test_auth_invalid(page:Page):
    page.goto("https://lebyy.com/practice/auth.html",wait_until="domcontentloaded")
    page.locator("#username").fill("locked_user")
        
    page.locator("#password").fill("Lebyy@Lab1")
    page.get_by_role("button",name="Sign in").click()
    expect(page.locator("#authAlert")).to_have_text("This account is locked. Contact lab support.")
    expect(page).to_have_url(re.compile(r"auth\.html"))
