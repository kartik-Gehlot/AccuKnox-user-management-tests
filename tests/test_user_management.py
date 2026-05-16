from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_page import AdminPage


def test_login_and_open_admin():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        admin = AdminPage(page)

        # Login
        login.login("Admin", "admin123")

        # Navigate to Admin module
        admin.open_admin()

        browser.close()


def test_add_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        admin = AdminPage(page)

        login.login("Admin", "admin123")
        admin.open_admin()

        # Add a new user
        admin.add_user("karti", "Password@123")

        browser.close()

def test_search_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        admin = AdminPage(page)

        login.login("Admin", "admin123")
        admin.open_admin()

        # Search for the user created in test_add_user
        admin.search_user("karti")

        browser.close()


def test_edit_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        admin = AdminPage(page)

        login.login("Admin", "admin123")
        admin.open_admin()

        # Search and edit the user
        admin.search_user("karti")
        admin.edit_user("kartiiii")

        browser.close()


def test_validate_updated_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        admin = AdminPage(page)

        login.login("Admin", "admin123")
        admin.open_admin()

        # Search for the updated username
        admin.search_user("kartiiii")

        browser.close()


def test_delete_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        admin = AdminPage(page)

        login.login("Admin", "admin123")
        admin.open_admin()

        # Search and delete the updated user
        admin.search_user("kartiiii")
        page.wait_for_timeout(3000)
        admin.delete_user()

        browser.close()        