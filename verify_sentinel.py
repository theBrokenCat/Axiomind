import requests
import sys
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

BASE_URL = "http://127.0.0.1:8000"

def wait_for_server():
    print("Waiting for server to start...")
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    
    start_time = time.time()
    while time.time() - start_time < 10:
        try:
            response = session.get(f"{BASE_URL}/health")
            if response.status_code == 200:
                print("Server is up!")
                return True
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    return False

def test_sentinel():
    if not wait_for_server():
        print("Server failed to start.")
        sys.exit(1)

    print("\n--- Testing Sentinel (Auth Middleware) ---")

    # 1. Public Endpoint (Health Check)
    try:
        res = requests.get(f"{BASE_URL}/health")
        print(f"1. GET /health: {res.status_code} (Expected 200)")
        if res.status_code != 200:
            print(f"FAILED: Response {res.text}")
    except Exception as e:
        print(f"FAILED /health: {e}")

    # 2. Protected Endpoint - Missing Token
    try:
        res = requests.get(f"{BASE_URL}/api/v1/secure-test")
        print(f"2. GET /api/v1/secure-test (No Header): {res.status_code} (Expected 401)")
        if res.status_code != 401:
            print(f"FAILED: Response {res.text}")
    except Exception as e:
         print(f"FAILED No Header: {e}")

    # 3. Protected Endpoint - Invalid Token
    headers = {"Authorization": "Bearer invalid-token-123"}
    try:
        res = requests.get(f"{BASE_URL}/api/v1/secure-test", headers=headers)
        print(f"3. GET /api/v1/secure-test (Invalid Token): {res.status_code} (Expected 403)")
        if res.status_code != 403:
             print(f"FAILED: Response {res.text}")
    except Exception as e:
        print(f"FAILED Invalid Token: {e}")

    # 4. Protected Endpoint - Valid Token
    headers = {"Authorization": "Bearer axiomind-secret-key"}
    try:
        res = requests.get(f"{BASE_URL}/api/v1/secure-test", headers=headers)
        # Expected 404 because the route doesn't exist, BUT it means it passed the middleware (401/403).
        print(f"4. GET /api/v1/secure-test (Valid Token): {res.status_code} (Expected 404)")
        if res.status_code != 404:
             print(f"FAILED: Response {res.text}")
    except Exception as e:
        print(f"FAILED Valid Token: {e}")

if __name__ == "__main__":
    test_sentinel()
