#!/usr/bin/python
import sys

from pip._vendor.distlib.compat import raw_input

raw_input("\n\nPress the enter key to exit.")
try:
    print("There was an error writing to")
    print("Enter When finished")
    while file_text != file_finish:
        file_text = raw_input("Enter text: ")
    if file_text == file_finish:
        # close the file
        file.close
        break
    file.write(file_text)
    file.write("\n")
file.close()
file_name = raw_input("Enter filename: ")
if len(file_name) == 0:
    print( "Next time please enter something")
    sys.exit()
try:
    file = open(file_name, "r")
except IOError:
    print ("There was an error reading file")
    sys.exit()
file_text = file.read()
file.close()
print (file_text)