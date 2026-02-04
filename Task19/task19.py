import json

json_string='{"name":"Gemini","status":"active"}'

parsed_json=json.loads(json_string)

print(parsed_json["status"])