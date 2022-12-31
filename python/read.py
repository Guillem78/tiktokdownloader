# Using readlines()
file1 = open("/srv/tiktokdownloader/src/urls.conf", "r")
Lines = file1.readlines()

count = 0
# Strips the newline character
mydata = ['urls']
for line in Lines:
    count += 1
    mydata.append("Line{}: {}".format(count, line.strip()))
    print("Line{}: {}".format(count, line.strip()))

print (" Paco")
print ("Data is: ", mydata )
