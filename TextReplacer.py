"""
TextReplacer 

Allows the user to replace the text within a single file (or all of the files within a single directory).

Requires Python 3
"""
import os, fileinput

#List to contain all characters/words defined by the user to be stripped from a document
initlist = []
dictionary = {}

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

Appends words/characters to a global dictionary, mapping input to text to be replaced by. There are exception handlers in place to prevent blank input from wiping a
file clean of text (and instead treats blanks as deletions).
"""
def append():
    try:
        before = input("Designate a word or a set of characters to replace: ")
    except SyntaxError:
        before = ""
    try:
        after = input("Designate a word or a set of characters to replace " + before +" with (if you want to remove it completely, just leave the text field blank): ")
    except SyntaxError:
        after = ""
    dictionary[before] = after
    cont2 = input("Would you like to designate another word or a set of characters to strip from the document? y/n: ")
    if (cont2 is "y") or (cont2 is "Y"):
        append()

#Runtime
print ("This application will strip inserted characters from a designated document, or from the documents within a designated file directory.")
initlist = init()
append()

text = "line"
for b, a in dictionary.items():
    text += ".replace(%r, %r)" % (b, a)
text += ".strip()"

#Open/Write to file
#Single-file operations
if initlist[0] is "1":
    path = initlist[1] + "\\" + initlist[2]
    with fileinput.FileInput(path, inplace=1) as myfile:
        for line in myfile:
            print (eval(text))
#Directory-based operations
elif initlist[0] is "2":
    path = initlist[1]
    for filename in os.listdir(initlist[1]):
        with fileinput.FileInput(path + "\\" + filename, inplace=1) as myfile:
            for line in myfile:
                print (eval(text))
print ("Done!")
#Opens the file if a single file is modified, and opens the file explorer where the directory had its files modified
subprocess.call(r"explorer " + path, shell=True)
