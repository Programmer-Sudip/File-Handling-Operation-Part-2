# create a new file
new_file = open('New_file1', 'x')
new_file.close()

# check if a file exists
import os
print("Checking if my_file exists or not ...")
if os.path.exists('new_file'):
    os.remove("my_file.txt")

else:
    print("The file does not exist")

#create a new if it does not exists
my_file = open('my_file.txt', 'w')
my_file.write("HI! I am Penguin and I am 1 year old")
my_file.close()

# delete file named  Codingal
os.remove('Codingal.txt')

# delete the folder
os.rmdir('Folder')