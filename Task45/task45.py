import requests

urls = [
    "https://mock.httpstatus.io/404",
    "https://mock.httpstatus.io/200",
    "https://mock.httpstatus.io/204",
    "https://mock.httpstatus.io/404",
    "https://mock.httpstatus.io/304",
    "https://mock.httpstatus.io/504",
]

def health_check(url:str):
    try:
        res=requests.get(url,timeout=5)
        if res.status_code ==200:
            print(f"{url} -> Website is Live.")
        else:
            print(f"{url} -> Website Error: {res.status_code}")
    except Exception as e:
        print(f"{url} -> Error: {e}")


for url in urls:
    health_check(url)