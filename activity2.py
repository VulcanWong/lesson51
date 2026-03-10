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
