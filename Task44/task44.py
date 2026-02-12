import requests


try:
    res=requests.get("http://13.232.3.65/", timeout=5)
    if res.status_code == 200:
        print("Website is Live.")
    else:
        print(f"Website Error: {res.status_code}")
except Exception as e:
    print(f"Error: {e}")