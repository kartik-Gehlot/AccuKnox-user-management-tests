class AdminPage:
    def __init__(self, page):
        self.page = page

    def open_admin(self):
        # Open Admin module
        self.page.get_by_role("link", name="Admin").click()

        # Wait until User Management page loads
        self.page.get_by_role("button", name="Add").wait_for()

    def add_user(self, username, password):
        # Click Add
        self.page.get_by_role("button", name="Add").click()

        # Wait for form to load
        self.page.get_by_role("button", name="Save").wait_for()

        # Select User Role = ESS
        self.page.locator(".oxd-select-text").nth(0).click()
        self.page.get_by_role("option", name="ESS").click()

        # Select Employee Name
        self.page.get_by_placeholder("Type for hints...").fill("a")
        self.page.wait_for_timeout(2000)
        self.page.locator(".oxd-autocomplete-option").first.click()

        # Select Status = Enabled
        self.page.locator(".oxd-select-text").nth(1).click()
        self.page.get_by_role("option", name="Enabled").click()

        # Enter Username
        self.page.locator("input").nth(2).fill(username)

        # Enter Password and Confirm Password
        self.page.locator("input[type='password']").nth(0).fill(password)
        self.page.locator("input[type='password']").nth(1).fill(password)

        # Save
        self.page.get_by_role("button", name="Save").click()

        # Wait until back on User Management page
        self.page.get_by_role("button", name="Add").wait_for()

    def search_user(self, username):
        # Clear and fill username search field
        username_field = self.page.locator("input").nth(1)
        username_field.fill(username)

        # Search
        self.page.get_by_role("button", name="Search").click()

        # Wait for table or message to load
        self.page.wait_for_timeout(2000)

    def edit_user(self, new_username):
        # Click first Edit icon
        self.page.locator("button i.bi-pencil-fill").first.click()

        # Wait for edit form
        self.page.get_by_role("button", name="Save").wait_for()

        # Update username
        username_field = self.page.locator("input").nth(2)
        username_field.fill(new_username)

        # Save changes
        self.page.get_by_role("button", name="Save").click()

        # Wait until back on User Management page
        self.page.get_by_role("button", name="Search").wait_for()

    def delete_user(self):
        # Click first Delete icon
        self.page.locator("button i.bi-trash").first.click()

        # Wait for confirmation popup
        self.page.wait_for_timeout(2000)

        # Confirm deletion (press Enter)
        self.page.keyboard.press("Enter")

        # Wait for popup to close
        self.page.wait_for_timeout(2000)