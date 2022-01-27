from formatters import *
from filesystem import *
import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Usage: call %s filename.csv secondFilename.csv"%sys.argv[0])
else:
    inputFile = sys.argv[1]
    secondFile = sys.argv[2]
    outputPath = split(inputFile, 1)
    secondOutput = os.path.join(outputPath, "mergedtranslation.csv")
    outputPath = os.path.join(outputPath, "concattranslation.csv")

    firstFile = pd.read_csv(inputFile, sep = ';')
    secondFile = pd.read_csv(secondFile, sep = ';')
    frame = pd.DataFrame(firstFile)
    frame2 = pd.DataFrame(secondFile)

    firstColumns = set(frame.columns.values.tolist())
    secondColumns = set(frame2.columns.values.tolist())

    print("The first file contains", len(frame.index), "touples, while the second contains", len(frame2.index) ," touples.")

    subtraction = firstColumns - secondColumns
    if len(subtraction) > 0:
        #they are different
        intersection = firstColumns.intersection(secondColumns)
        if len(intersection) > 0:
            missingColumn = secondColumns - intersection
            for item in missingColumn:
                frame[item] = "TODO"
        
        secondIntersection = secondColumns.intersection(firstColumns)
        if len(intersection) > 0:
            missingColumn2 = firstColumns - intersection
            for item in missingColumn2:
                frame2[item] = "TODO"
    
    concatFrame = pd.concat([frame, frame2], ignore_index=True, verify_integrity= True).drop_duplicates(subset = "keys")
    concatFrame.sort_values(by='keys').to_csv(outputPath, index = False, sep = ';')

    #mergedFrame = pd.merge(firstFile, secondFile).sort_values(by='keys')
    #mergedFrame.to_csv(secondOutput, index = False, sep = ';')
  