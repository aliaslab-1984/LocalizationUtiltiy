from formatters import *
import pandas as pd
import os
import sys
from filesystem import *

def buildAndroidFile(rawList, columnName, basePath):
    finalString = xmlHeaderString() + "\n" + rawList + "\n" + xmlFooterString()
    path = os.path.join(basePath, "Android/values-%s"%columnName)
    print("Saving Android translation to: ", path)
    try:
        os.makedirs(path, exist_ok = True)
        writeFile(path, "strings.xml", finalString)
    except OSError as error:
        print(error)
        return

def buildiOSFile(rawList, columnName, basePath):
    path = os.path.join(basePath, "iOS/%s.lproj/"%columnName)
    print("Saving iOS translation to: ", path)
    try:
        os.makedirs(path, exist_ok = True)
        writeFile(path, 'Localizable.strings', rawList)
    except OSError as error:
        print(error)
        return

if len(sys.argv) == 1:
    print("Usage: call localizationUtility.py filename.csv")
else:
    inputFile = sys.argv[1]
    outputPath = os.getcwd()
    outputPath = os.path.join(outputPath, "Translation")

    if inputFile == "-help" or inputFile == "-h":
        print("Usage: call localizationUtility.py filename.csv")
    else:
        print("Parsing", inputFile)
        df = pd.read_csv(inputFile, sep=';')
        columns = list(df.columns)
        columnCount = len(columns)
        keysColumn = columns.pop(0)
        keys = df.loc[:, keysColumn]

        for column in columns:
            pair = zip(keys, df.loc[:, column])
            androidString = ""
            iOSstring = ""
            for key, value in pair:
                androidString += formatXML(key, value)
                iOSstring += formatiOSString(key, value)
                androidString += "\n"
                iOSstring += "\n"
            buildAndroidFile(androidString, column, outputPath)
            buildiOSFile(iOSstring, column, outputPath)
