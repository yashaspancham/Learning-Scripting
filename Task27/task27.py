import os

file_write_bool = os.access("audit_log.txt", os.W_OK)

if file_write_bool:
    print("File is writable")
else:
    os.chmod("audit_log.txt",0o600)
    print("Read and write permission added")
