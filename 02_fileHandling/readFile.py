# open a file
# provide file path and the mode in which file is being opened (read, write, append or read+write)
text_file = open("d://python/02_fileHandling/abc.txt", "r")

# check whether the file is readable or not
print(text_file.readable())

# read a single line from file and move the cursor to the next line
print(text_file.readline())

# return a list of all the lines in the file and move the cursor to end of the file
print(text_file.readlines())

# lop over the list to print each line
for line in text_file.readlines():
    print(line)

# read complete file in once and move the cursor to the end of the fle
print(text_file.read())

# close the file
text_file.close()