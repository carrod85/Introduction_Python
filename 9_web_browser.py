import webbrowser
import time
open_times=5

for x in range (open_times):
    webbrowser.open('http://www.google.com',x)
    time.sleep(5)