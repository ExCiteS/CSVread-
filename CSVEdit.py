import csv
import os
from tkinter.filedialog import askopenfilename

## Modify this line to change logic of fields to keep
keepers = ("StartTime-LocalYYYYMMDD_HHMMSS", "EndTime-LocalYYYYMMDD_HHMMSS", "-Value", ".Latitude", ".Longitude", ".Accuracy")

fileName, fileExtension = os.path.splitext(askopenfilename(filetypes=[("Sapelli CSV", "*.csv")]))
oldFile = fileName + fileExtension
newFile = fileName + '_new' + fileExtension
fieldsToKeep = []

with open(oldFile) as infile, open(newFile, "w", newline="") as outfile:
    r = csv.DictReader(infile)
    for fieldName in r.fieldnames:
        if fieldName.endswith(keepers):
            fieldsToKeep.append(fieldName)
    w = csv.DictWriter(outfile, fieldsToKeep, extrasaction="ignore")
    w.writeheader()
    for row in r:
        w.writerow(row)
