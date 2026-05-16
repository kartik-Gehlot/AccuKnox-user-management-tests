import requests
from datetime import datetime

# URL to monitor
URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


def check_application(url):
    try:
        response = requests.get(url, timeout=10)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if response.status_code == 200:
            print(f"[{timestamp}] Application Status: UP")
            print(f"HTTP Status Code: {response.status_code}")
        else:
            print(f"[{timestamp}] Application Status: DOWN")
            print(f"HTTP Status Code: {response.status_code}")

    except requests.exceptions.RequestException as error:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Application Status: DOWN")
        print(f"Error: {error}")


if __name__ == "__main__":
    check_application(URL)