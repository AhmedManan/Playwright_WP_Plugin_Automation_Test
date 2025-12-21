import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        # browser = pw.chromium.launch(headless=False, slow_mo=500)
        browser = pw.chromium.launch(headless=True, slow_mo=500)  # To run tests through GitHub workflow
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
