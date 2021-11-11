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

    firstFile = pd.read_csv(inputFile)
    secondFile = pd.read_csv(secondFile, sep=';')
    frame = pd.DataFrame(firstFile)
    frame2 = pd.DataFrame(secondFile)
    
    concatFrame = pd.concat([frame, frame2], ignore_index=True, verify_integrity= True).sort_values(by='keys').drop_duplicates()
    concatFrame.to_csv(outputPath, index = False)

    mergedFrame = pd.merge(firstFile, secondFile).sort_values(by='keys')
    mergedFrame.to_csv(secondOutput, index = False)
  
