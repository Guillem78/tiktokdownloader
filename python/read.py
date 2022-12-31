import pandas
# Using readlines()
# file1 = open("C:\Users\bonamusg\developer\tiktokdownloader\src\urls.conf", "r")
pandas.read_csv(r"C:\Users\bonamusg\developer\tiktokdownloader\src\urls.conf")
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
