import urllib.request
import urllib.parse
import json

url = "http://localhost:8000/analyze/"
data = urllib.parse.urlencode({"text_input": "This is a test request to verify the AI module is functioning correctly."}).encode()

req = urllib.request.Request(url, data=data, method="POST")
print(f"Testing AI Endpoint: {url}")

try:
    with urllib.request.urlopen(req) as response:
        status = response.status
        body = response.read().decode()
        print(f"Status: {status}")
        print(f"Response: {body}")
        
    if status == 200:
        print("SUCCESS: AI Endpoint is responding.")
    else:
        print("FAILURE: AI Endpoint returned non-200 status.")

except Exception as e:
    print(f"ERROR: Failed to connect or receive response. {e}")
