import json

json_string='{"server": {"id": "aws-123", "status": "running", "network": {"ip": "10.0.0.5", "type": "private"}}}'

json_json=json.loads(json_string)

print(json_json["server"]["network"]["ip"])