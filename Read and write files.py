fw = open('sample.txt', 'w')
fw.write('This text will be written in a new file\n')
fw.write('This will be on the next line\n')
fw.close()  # write cmd needs to be closed to save pc memory

fr = open('sample.txt', 'r')
variable = fr.read()  # put the text in the file in a variable
print(variable)
fr.close()


# to do this with a file on the pc: fw open = (r'/User/Desktop/sample.txt', w)﻿
