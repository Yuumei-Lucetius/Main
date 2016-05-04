
# coding: utf-8

# In[9]:

import os, fileinput

#Array to contain all characters/words defined by the user to be stripped from a document
initarray = myarray = []

"""
init()

Collects the file directory, name and optional character stripping settings designated by the user, and will loop/restart
whenever an invalid file directory or name is submitted to prevent errors.
Returns an array consisting of the directory, file name and option of whether to open a single file or all of the files
within the designated file directory.
"""
def init():
    dirarray = []
    dir1 = input("Designate a file directory (Note: do not end it with a backslash): ")
    if not os.path.isdir(dir1):
        print (dir1 + " is not a valid directory.")
        init()
    cont1 = input("Would you like to strip words or characters from a single file (1), or from all the files within a designated file directory (2)? 1/2: ")
    if cont1 is "1": 
        dir2 = input("Enter a file name with its extension (i.e. document.txt): ")
        if not os.path.isfile(dir1 + "\\" + dir2):
            print (dir2 + " is not a valid file in the directory " + dir1 + ". You will be returned to the beginning.")
            init()
    dirarray.append(cont1)
    dirarray.append(dir1)
    dirarray.append(dir2)
    return dirarray
    #spec = input("Would you like to strip non-alphanumeric characters? y/n: ")

"""
append()

Appends words/characters to a global array.
"""
def append():
    word = input("Designate a word or a set of characters to strip from the document: ")
    cont2 = input("Would you like to designate another word or a set of characters to strip from the document? y/n: ")
    if (cont2 is "y") or (cont2 is "Y"):
        myarray.append(word)
        append()
    else:
        myarray.append(word)

#Runtime
print ("This application will strip inserted characters from a designated document, or from the documents within a designated file directory.")
initarray = init()
append()

#Open/Write to file
if initarray[0] is "1":
    with fileinput.FileInput(initarray[1] + "\\" + initarray[2], inplace=1) as myfile:
        for line in myfile:
            for i in myarray:
                 print(line.replace(i, ""))
    print ("Done!")

