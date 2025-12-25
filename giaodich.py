import requests

url = "https://mobile.acb.com.vn/api/login"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile)",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-API-KEY": "FAKE_API_KEY_123456789"
}

payload = {
    "username": "test_user_001",
    "password": "TestPassword@123"
}

try:
    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=10
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print("Request error:", e)


# acb.com.vn
# cuong@acb.com.vn