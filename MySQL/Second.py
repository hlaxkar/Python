import time
import os

while True:
    if os.path.exists("JK.txt"):
        with open("JK.txt") as myfile:
            print(myfile.read())
    else: print("The file doesn't exits!")
    time.sleep(5)        