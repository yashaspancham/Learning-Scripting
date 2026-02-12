import pwd

try:
    user_details=pwd.getpwnam("developer")
    print("User found.")
except KeyError as e:
    print("User missing - please create it.")