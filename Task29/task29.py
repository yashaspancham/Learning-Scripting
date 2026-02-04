import os
from dotenv import load_dotenv

load_dotenv()

env_var=os.getenv("APP_ENV")
print(env_var)