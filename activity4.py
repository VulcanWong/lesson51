with open('my_file.txt') as fp:
    data1 = fp.read()

with open('New_File.txt') as fp:
    data2 = fp.read()

data1 += "\n"
data1 += data2
print("Merging two files.....")
with open ('MergedFile.txt', 'w')as fp:
    fp.write(data1)
