from datetime import datetime

now=datetime.now()
filename_date = now.strftime("%Y-%m-%d-%H-%M")

print(f"backup_[{filename_date}].zip")