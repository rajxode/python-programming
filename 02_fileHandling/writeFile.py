# open file in append mode
text_file = open("d://python/02_fileHandling/abc.txt", "a")

# append the following line at the end of the file starting from new line
text_file.write("\nB category ke C class log")

# create a new file
text_file2 = open("d://python/02_fileHandling/abc2.txt","w")

# write the content file 
# if file has some content already, it will be over written
text_file2.write("Main langotiye Jeetu ka mara hua yar hoon. !!")
text_file2.write("\nMain hoon gullu taxi driver!!")

# closing the files
text_file.close()
text_file2.close()