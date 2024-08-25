import os
import time

os.system("pip install pyinstaller")
os.system("pyinstaller --icon=/ico/exe.ico --onefile main.py")
print("File made in dist/\nExecuting in 5 seconds.")
time.sleep(5.0)
os.system("cd dist")
os.system("./main")