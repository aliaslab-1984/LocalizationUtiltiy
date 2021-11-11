from formatters import *
from filesystem import *
import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Usage: call %s filename.xml it"%sys.argv[0])
else:
    inputFile = sys.argv[1]
    languageName = sys.argv[2]
    outputPath = split(inputFile, 3)
    outputPath = os.path.join(outputPath, "translation.csv")

    parsedKeys = list()
    parsedValues = list()

    pairs = extractXMLKeyAndValue(inputFile)
    parsedKeys = pairs[0]
    parsedValues = pairs[1]

    if os.path.exists(outputPath):
        file = pd.read_csv(outputPath)
        frame = pd.DataFrame(file)
        if languageName not in frame.columns:
            frame[languageName] = parsedValues
            frame.to_csv(outputPath, index = False)
        else:
            tableData = {"keys": parsedKeys,
            languageName: parsedValues}

            newFrame = pd.concat([frame, pd.DataFrame(tableData)], ignore_index=True, verify_integrity= True).sort_values(by='keys')
            newFrame.to_csv(outputPath, index = False)
    else:
        tableData = {"keys": parsedKeys,
            languageName: parsedValues
            }

        frame = pd.DataFrame(tableData)

        frame.to_csv(outputPath, index = False)
