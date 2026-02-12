import os

api_key=os.environ.get("API_KEY")

if api_key!=None:
    print(f"API Key found: {api_key[:4]}***")
else:
    print(f"Error: API_KEY environmenr variable not set!")
