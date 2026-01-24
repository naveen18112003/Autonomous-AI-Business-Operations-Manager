import urllib.request
import urllib.error
import sys

BASE_URL = "https://autonomous-ai-business-operations-manager-16f44vhhc.vercel.app/api"

def test_endpoint(path):
    url = f"{BASE_URL}{path}"
    print(f"Testing {url}...")
    try:
        with urllib.request.urlopen(url) as response:
            print(f"Status: {response.getcode()}")
            content = response.read().decode('utf-8')
            print(f"Response: {content[:200]}...")
            return response.getcode() == 200
    except urllib.error.URLError as e:
        print(f"Failed: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

print("--- Starting API Tests (urllib) ---")

if not test_endpoint("/"):
    print("Root endpoint failed!")
    sys.exit(1)

if not test_endpoint("/docs"):
    print("Docs endpoint failed!")

print("\n--- API Tests Completed Successfully ---")
