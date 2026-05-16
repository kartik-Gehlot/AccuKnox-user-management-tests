class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.goto(self.URL)
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

        # Wait until dashboard loads
        self.page.get_by_role("link", name="Admin").wait_for()