import json
import requests


def JSON_data():
    hostname = "prod-web-01"
    cpu_usage = 45
    status = "healthy"
    data = {"host": hostname, "cpu": cpu_usage, "status": status}

    return data


data = JSON_data()
url = "https://webhook.site/6b5c8d27-f704-4b0d-8801-1b2338650171"

requests.post(url, json=data,  timeout=5)
