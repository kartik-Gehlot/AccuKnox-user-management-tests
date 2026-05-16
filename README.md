# AccuKnox User Management Tests

This project automates the User Management end-to-end flow in OrangeHRM using Playwright with Python and the Page Object Model (POM).

## Application Under Test
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

## Login Credentials
- Username: Admin
- Password: admin123

## Project Structure
AccuKnox-user-management-tests/
├── pages/
│   ├── login_page.py
│   └── admin_page.py
├── tests/
│   └── test_user_management.py
├── README.md
├── requirements.txt
└── manual_test_cases.xlsx

## Setup Steps

### 1. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate

## Install Dependencies
pip install -r requirements.txt
playwright install

## Run the Test Cases
pytest -v

Test Scenarios Automated
Login and Navigate to Admin Module
Add a New User
Search the Newly Created User
Edit User Details
Validate Updated Details
Delete the User