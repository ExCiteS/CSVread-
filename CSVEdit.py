import csv
import os
from tkinter.filedialog import askopenfilename
#CHANGE NEXT LINE TO CONTROL WHICH FIELDS ARE PRINTED
fieldsToPrint = [ 0, 2] #Remember to start counting from 0!
#End change

a = []
i=0
b=''

fileName, fileExtension = os.path.splitext(askopenfilename( filetypes=[("Sapelli CSV","*.csv")]));
newFile = fileName + '_new' + fileExtension;

csvReader = csv.reader(open(fileName + fileExtension), delimiter=',')
for row in csvReader:
	a.append(row)
outputCSV = open(newFile, 'w',newline='')
writer = csv.writer(outputCSV)

for i in range(0, len(a)):
        rowToWrite = ""
        for j in fieldsToPrint:
                rowToWrite += a[i][j]
        writer.writerow(rowToWrite)
outputCSV.close()
quit()

