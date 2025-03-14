#File Input/Output

"""
Python can be used to perform operations on a file.( read & write data )
Types of files
1. Text Files: .txt, .docx, .log etc
2. Binary Files: .mp4, .mov, .png, .jpeg etc
"""

#Open, Read and Close file
"""
Syntax
f = open("file_name if same folder, file_name with path if other folder", "mode")
modes:
r - read
w - write after truncating
x - create new file and write
a - write after existing data

f.readline() - read file line by line
"""

f = open("demo.txt", "r")
data = f.read() #read() is used to get all the data along with type
print(data)
f.close()

f = open("demo.txt", "w")
f.write("I want to learn Python tomorrow.")
f.close()

f = open("demo.txt", "a")
f.write("\n Hello Midhun, welcome to Python lecture.")
f.close()

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)