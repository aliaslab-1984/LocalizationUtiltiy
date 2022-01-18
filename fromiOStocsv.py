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
        # print("Red line: ", item)
        pair = extractiOSKeyAndValue(item)
        if pair != None:
            # print("Red key: ", pair[0])
            # print("Red value: ", pair[1])
            parsedData.append(pair)
            parsedKeys.append(pair[0])
            parsedValues.append(pair[1])

    print("Red ", len(parsedData), "pairs.")
    

    tableData = {"keys": parsedKeys,
            languageName: parsedValues
            }

    if os.path.exists(outputPath):
        print("Found an existing translation file, merging..")
        file = pd.read_csv(outputPath, sep = ';')
        existingDataFrame = pd.DataFrame(file).sort_values(by='keys', ignore_index = True)

        newDataFrame = pd.DataFrame(tableData).sort_values(by='keys', ignore_index = True)
        mergedFrame = pd.merge(existingDataFrame, newDataFrame).sort_values(by='keys')
        mergedFrame.to_csv(outputPath, index = False, sep = ';')
    else:
        print("Exporting to:", outputPath)
        frame = pd.DataFrame(tableData).sort_values(by='keys', ignore_index = True)

        frame.to_csv(outputPath, index = False, sep = ';')

print("Exported to:", outputPath)