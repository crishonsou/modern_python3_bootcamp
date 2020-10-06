# r - Read
# w - Write (previous content removed)
# a - Append (next line, previous content not removed)
# r+  Read and Write to a file


#with open("text.txt", "a") as file:
#    file.write("APPENDING LATTER!!!!\n")

with open('text.txt', 'r+') as file:
    file.write('Added USING r+')
