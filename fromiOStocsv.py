from formatters import *
from filesystem import *
import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Usage: call fromiOStocsv.py filename.strings it")
else:
    inputFile = sys.argv[1]
    languageName = sys.argv[2]
    outputPath = split(inputFile, 3)
    outputPath = os.path.join(outputPath, "translation.csv")

    data = readFilePerLine(inputFile)
    parsedData = list()
    parsedKeys = list()
    parsedValues = list()

    for item in data:
        pair = extractiOSKeyAndValue(item)
        parsedData.append(pair)
        parsedKeys.append(pair[0])
        parsedValues.append(pair[1])

    if os.path.exists(outputPath):
        file = pd.read_csv(outputPath)
        frame = pd.DataFrame(file)
        if languageName not in frame.columns:
            frame[languageName] = parsedValues

        frame.to_csv(outputPath, index = False)
    else:
        tableData = {"keys": parsedKeys,
            languageName: parsedValues
            }

        frame = pd.DataFrame(tableData)

        frame.to_csv(outputPath, index = False)
