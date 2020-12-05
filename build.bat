@echo off
Copy ".\jieba\dict.txt" ".\dict.txt"
Copy ".\jieba\analyse\idf.txt" ".\idf.txt"
pyinstaller --onefile --nowindowed --noconsole ExpressInfo.py
Copy ".\dist\ExpressInfo.exe" ".\ExpressInfo.exe"