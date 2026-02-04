from datetime import datetime
import shutil

current_date=datetime.now().strftime("%Y%m%d_%H%M")
shutil.make_archive("etc_backups_["+current_date+"]","gztar","backups")
shutil.rmtree("backups")