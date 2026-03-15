file = open('homework.txt')
print(file.read())
file.close()

file = open('hi.txt')
print(file.read())
file.close()

with open('Codingal.txt', 'w')as file:
    file.write("hi! i am penguin and i am 1yr old")
file.close()


with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are.....")
    for line in data:
        word = line.split()
        print(word)
file.close()
new_file = open('New_File.txt', 'x')
new_file.close()
import os 
print("checking if my_file exist or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")


my_file = open("my_file.txt", 'w')
my_file.write("hi!i am penguin and i am  1yr old")
my_file.close()


os.remove('codingal.txt')


os.rmdir('Folder')
outputFile = open('UpdatedFile.txt', "w")
inputFile = open('Repeated.txt', "r")
lines_seen_so_far = set()
print("Eliminating duplicate lines.....")
for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)
inputFile.close()
outputFile.close()
with open('my_file.txt') as fp:
    data1 = fp.read()

with open('New_File.txt') as fp:
    data2 = fp.read()

data1 += "\n"
data1 += data2
print("Merging two files.....")
with open ('MergedFile.txt', 'w')as fp:
    fp.write(data1)
