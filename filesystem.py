import os, sys

# make dirs with mode
def writeFile(path, name, finalString):
    fd = open(os.path.join(path, name), "w")
    fd.write(finalString)
    fd.close()
