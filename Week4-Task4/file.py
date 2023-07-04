
##with open("sample.txt","x") as file:
##    file.write("age is 24")


##with open("samples.txt","x") as file:
##    file.write("age is 24")

##file = open("sample.txt", "r")
##position = file.tell()
##print("Current position:", position)


##file = open("samples.txt", "r")
##position = file.tell()
##file.write("ufgwuguf")
##print("Current position:", position)

##file = open("samples.txt", "w")
##position = file.tell()
##file.write("ufgwuguf")
##print("Current position:", position)


file = open("example.txt", "w+")
file.write("In this example, we open the file in write mode and use the write() method to write the string  to the file.")
##           After that, we call the tell() method to get the current position of the file pointer. However,
##           since we opened the file in write mode, the file pointer is at the end of the file after writing the content.
##           Therefore, the tell() method will return the file's size, indicating the end position.""")
# Read the first line
line1 = file.readline()
print("First line:", line1)

# Get the current position of the file pointer
position = file.tell()
print("Current position:", position)

# Read the second line
line2 = file.readline()
print("Second line:", line2)

# Get the updated position of the file pointer
position = file.tell()
print("Current position:", position)

file.close()
