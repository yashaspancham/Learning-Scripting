import os

user_name=os.environ.get("USER_NAME","Guest")

print(f"Hello, {user_name}")