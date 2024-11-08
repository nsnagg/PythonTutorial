fname = input("\nEnter file name:  ")

try:
    fhand = open("FreeCodeCamp/res/" + fname)
except:
    print("File cannot be opened:", fname)
    quit()

for line in fhand:
    line = line.rstrip()
    if not "@uct.ac.za" in line:
        continue
    print(line)
    
    
