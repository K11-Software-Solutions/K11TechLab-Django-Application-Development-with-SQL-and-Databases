# Playwright test for Django authentication UI
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


def test_homepage_and_login(browser):
    page = browser.new_page()
    # Change the URL if your dev server runs on a different port
    page.goto("http://127.0.0.1:8000/onlinecourse/")
    assert "Course" in page.content() or "course" in page.content()
    # Go to login page (update selector if needed)
    page.goto("http://127.0.0.1:8000/accounts/login/")
    # Fill login form (update selectors as needed)
    page.fill('input[name="username"]', 'testuser')
    page.wait_for_timeout(200)  # Wait 200ms for password field to be ready
    page.fill('input[name="password"]', 'testpass123')
    page.wait_for_timeout(200)  # Wait 200ms before clicking submit
    page.click('button[type="submit"]')
    # Wait for navigation or logout link to appear
    page.wait_for_load_state('networkidle')
    # Optionally, wait for the logout link to appear
    # page.wait_for_selector('a[href="/accounts/logout/"]')
    assert "Logout" in page.content() or "logout" in page.content()
    page.close()
