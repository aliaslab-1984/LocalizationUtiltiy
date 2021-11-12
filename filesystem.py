import os, sys

def outputPath(inputFile, defaultPath, splits):
    if len(sys.argv) > 3:
        return sys.arg[3]
    else: 
        outputPath = split(inputFile, splits)
        outputPath = os.path.join(outputPath, defaultPath)

# make dirs with mode
def writeFile(path, name, finalString):
    fd = open(os.path.join(path, name), "w")
    fd.write(finalString)
    fd.close()

def readFile(path):
    fd = open(path, "r")
    data = fd.read().replace('\n', '')
    fd.close()
    return data

def readFilePerLine(path):
    # open the data file
    file = open(path)
    # read the file as a list
    data = file.readlines()
    # close the file
    file.close()
    return data

def split(path, times):
    output = path
    for i in range(times):
        output = os.path.split(output)[0]
    
    return output