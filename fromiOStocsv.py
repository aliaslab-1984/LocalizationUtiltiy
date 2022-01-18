from formatters import *
from filesystem import *
import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Usage: call %s filename.strings [language] optional_output_path"%sys.argv[0])
else:
    inputFile = sys.argv[1]
    languageName = sys.argv[2]
    outputPath = outputPath(inputFile, "translation.csv", 1)
    data = readFilePerLine(inputFile)
    parsedData = list()
    parsedKeys = list()
    parsedValues = list()

    for item in data:
        print("Red line: ", item)
        pair = extractiOSKeyAndValue(item)
        if pair != None:
            print("Red key: ", pair[0])
            print("Red value: ", pair[1])
            parsedData.append(pair)
            parsedKeys.append(pair[0])
            parsedValues.append(pair[1])

    print("Red ", len(parsedData), "pairs.")
    print("Exporting to:", outputPath)

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
