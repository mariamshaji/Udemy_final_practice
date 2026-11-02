from playwright.sync_api import Page,expect
import time



'''def test_single_file_upload(page:Page):
    page.goto("https://lebyy.com/practice/attachments.html")

    page.locator("#evidence").set_input_files("/Users/mariampshaji/Documents/Playwright/udemy_final_project/tests/flow5.txt")
    time.sleep(2)
    expect(page.locator("#selectedName")).to_have_text("flow5.txt")
    page.get_by_test_id("upload-submit").click()
    time.sleep(3)
    expect(page.locator("#uploadAlert")).to_have_text("Attached locally: flow5.txt")'''


'''def test_multiple_file_upload(page:Page):
    page.goto("https://lebyy.com/practice/attachments.html")

    page.locator("#multiEvidence").set_input_files([
        "/Users/mariampshaji/Documents/Playwright/udemy_final_project/tests/flow4.txt",
        "/Users/mariampshaji/Documents/Playwright/udemy_final_project/tests/flow5.txt"]
    )

    time.sleep(2)

    expect(page.get_by_test_id("selected-multi-names")).to_contain_text("flow4.txt, flow5.txt")
    time.sleep(2)

    page.locator("#attachMulti").click()
    time.sleep(2)'''


'''def test_download_txt_file_with_correct_name_and_content(
    page: Page) -> None:
    page.goto("https://lebyy.com/practice/attachments.html")

    with page.expect_download() as download_info:
        page.get_by_test_id("download-txt").click()

    download = download_info.value

    assert download.suggested_filename == "lebyy-sample-evidence.txt"

    file_path = download.path()

    with open(file_path,"r",encoding="utf-8") as file:
        content = file.read()

    assert "Sample evidence file for Lebyy Practice Lab downloads." in content'''

