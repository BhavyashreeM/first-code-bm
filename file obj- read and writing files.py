#File objects

"""
#First approach

file = open("C:\\Users\\Bhavyadivya\\Anaconda python\\DATA SCIENCE Practice\\filename.txt", 'r')
print(file.read()) # gives all the content in the file-generally not recommended for large file since it may cause performance issue
print(file.readline()) #gives line by line data from the file
print(file.readlines()) #gives all the lines in the  file as a list

"""
#Another method for file manipulation
#since with the first approach of direct read/write, we might need to close the file exclusively with 'File_name.close()' method
#But with this 'with open() ' it will automatically closes i.e., content out of that identation will not be included so file
# is accessable with in this method

"""
with open('new_file.txt','w') as file:
    #file_cont = file.write('This is the first line')  #to write single line, this will overwrite the exixting content
    file_cont = ['This is the first line\n', 'This is the Second line\n','This is third line\n','And this is fourth one\n']
    file.writelines(file_cont)

"""


with open('new_file.txt','r') as rf:
    with open('new_file2.txt','w') as wf:   # new_file2 is copy of new_file
        for line in rf:
            wf.write(line)