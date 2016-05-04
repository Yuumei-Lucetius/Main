import os, fileinput

#List to contain all characters/words defined by the user to be stripped from a document
initlist = mylist = []

"""
init()

Collects the file directory, name and optional character stripping settings designated by the user, and will loop/restart
whenever an invalid file directory or name is submitted to prevent errors.
Returns a list consisting of the directory, file name and option of whether to open a single file or all of the files
within the designated file directory.
"""
def init():
    dirlist = []
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
        dirlist.append(cont1)
        dirlist.append(dir1)
        dirlist.append(dir2)
    elif cont1 is not "2":
        #Return the user to the beginning, for they need to have selected a 1 or 2 to continue
        print ("As you have not specified whether to strip from a single (1) or multiple files (2), you will be returned to the beginning.")
        init()
    else:
        dirlist.append(cont1)
        dirlist.append(dir1)
    return dirlist
    #spec = input("Would you like to strip non-alphanumeric characters? y/n: ")

"""
append()

Appends words/characters to a global list.
"""
def append():
    word = input("Designate a word or a set of characters to strip from the document: ")
    mylist.append(word)
    cont2 = input("Would you like to designate another word or a set of characters to strip from the document? y/n: ")
    if (cont2 is "y") or (cont2 is "Y"):
        append()

#Runtime
print ("This application will strip inserted characters from a designated document, or from the documents within a designated file directory.")
initlist = init()
append()

#Open/Write to file
#Single-file operations
if initlist[0] is "1":
    with fileinput.FileInput(initlist[1] + "\\" + initlist[2], inplace=1) as myfile:
        for line in myfile:
            for i in mylist:
                print (line.replace(i, "").strip())
#Directory-based operations
elif initlist[0] is "2":
    for filename in os.listdir(initlist[1]):
        with fileinput.FileInput(initlist[1] + "\\" + filename, inplace=1) as myfile:
            for line in myfile:
                for i in mylist:
                    print (line.replace(i, "").strip())
print ("Done!")
