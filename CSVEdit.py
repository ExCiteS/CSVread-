import csv
import os
from tkinter.filedialog import askopenfilename
#CHANGE NEXT LINE TO CONTROL WHICH FIELDS ARE PRINTED
fieldsToKeep = ["StartTime-LocalYYYYMMDD_HHMMSS", "EndTime-LocalYYYYMMDD_HHMMSS", "Situation-Value", "Location.Latitude", "Location.Longitude", "Location.Altitude", "Location.Bearing", "Location.Accuracy"]
#End change

fileName, fileExtension = os.path.splitext(askopenfilename( filetypes=[("Sapelli CSV","*.csv")]));
oldFile = fileName + fileExtension;
newFile = fileName + '_new' + fileExtension;

with open(oldFile) as infile, open(newFile, "w", newline="") as outfile:
    r = csv.DictReader(infile)
    w = csv.DictWriter(outfile, fieldsToKeep, extrasaction="ignore")
    w.writeheader()
    for row in r:
        w.writerow(row)