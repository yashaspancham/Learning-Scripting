import json

hostname = "prod-web-01"
cpu_usage = 45
status = "healthy"
data = {"host": hostname, "cpu": cpu_usage, "status": status}

json_string = json.dumps(data,indent=4)

print(json_string)