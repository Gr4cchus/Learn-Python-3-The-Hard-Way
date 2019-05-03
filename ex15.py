from sys import argv    # from package sys, import feature argv

script, filename = argv # run with 1 argument

txt = open(filename)    # open file with 1st argument and save as a var

print(f"Here's your file {filename}:")  # print 1st argument
print(txt.read())   # read operation on txt(an open file)

txt.close()

print("Type the filename again:")
file_again = input("> ")    # a custom prompt that needs filename saved to var

txt_again = open(file_again)    # open the file and save as a new var

print(txt_again.read()) # print file contents

txt_again.close()