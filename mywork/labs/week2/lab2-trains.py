## WSAA
## Lab 2 - Trains

## Author: E. Qejvani

import requests
import csv
from xml.dom.minidom import parseString
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# check it works
# print (doc.toprettyxml()) #output to console comment this out once you know it works
# if I want to store the xml in a file. You can comment this out later

# array to store all the names of the tags we need to retrieve.
retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]

# storing data in  the xml file.
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)

    
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-r# adding the newline= '' parameter
with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
            train_writer.writerow(dataList)
        
