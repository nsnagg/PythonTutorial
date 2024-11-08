fname = input("Enter any existing filename:\n")
#fhandle = open("FreeCodeCamp/res/" + fname, "r")

try:
    with open("FreeCodeCamp/res/" + fname, "r") as file:
        print("File has opened for reading.")
except IOError:
    print("File has opened already")

