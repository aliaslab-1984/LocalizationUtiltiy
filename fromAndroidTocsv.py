from formatters import *
from filesystem import *
import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Usage: call %s filename.xml it optional_output_path"%sys.argv[0])
else:
    inputFile = sys.argv[1]
    languageName = sys.argv[2]
    outputPath = outputPath(inputFile, "translation.csv", 1)

    parsedKeys = list()
    parsedValues = list()

    pairs = extractXMLKeyAndValue(inputFile)
    parsedKeys = pairs[0]
    parsedValues = pairs[1]

    for i, val in enumerate(parsedValues):
         parsedValues[i] = invertXMLSpecialCharacters(val)

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
