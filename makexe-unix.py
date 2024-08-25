import os
import time

os.system("pip3 install pyinstaller")
os.system("pyinstaller --icon=/ico/exec.ico --onefile main.py")
print("File made in dist/\nExecuting in 5 seconds.")
time.sleep(5.0)
os.system("dist/main.exe")