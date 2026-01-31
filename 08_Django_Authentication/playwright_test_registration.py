# Playwright test for Django registration UI
import pytest
from playwright.sync_api import sync_playwright
import random
import string

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


def test_registration(browser):
    context = browser.new_context(record_video_dir=".")
    page = context.new_page()
    # Generate a random username for each test run
    rand_username = 'playwrightuser_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    page.goto("http://127.0.0.1:8000/accounts/register/")
    page.fill('input[name="username"]', rand_username)
    page.fill('input[name="password1"]', 'playwrightpass123')
    page.fill('input[name="password2"]', 'playwrightpass123')
    page.click('button[type="submit"]')
    page.wait_for_load_state('networkidle')
    page.screenshot(path="welcome_page.png")
    content = page.content()
    assert "Course" in content or "course" in content or "Welcome" in content
    page.close()
    context.close()
