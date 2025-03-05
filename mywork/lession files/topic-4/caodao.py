# Web Services and Applications - WSAA
# Topic 4 - part 3 - cso
from ast import Pass
import requests
import json

urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"
def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)
def getAll(dataset):
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json()

def getformatedAsFile(dataset):
    pass

def getFormated(dataset):
    data = getAll(dataset)
    ids = data["id"]
    values = data["value"]
    dimensions = data["dimension"]
    sizes = data["size"]
    
    for dim0 in range(0, sizes[0]):
        currentId = ids[0]
        index = dimensions[currentId]["category"]["index"][dim0]
        label = dimensions[currentId]["category"]["index"][index]
        print(label)
        for dim1 in range(0, sizes[1]):
            currentId = ids[1]
            index = dimensions[currentId]["category"]["index"][dim1]
            label = dimensions[currentId]["category"]["index"][index]
            print(label)
            for dim2 in range(0, sizes[2]):
                currentId = ids[2]
                index = dimensions[currentId]["category"]["index"][dim2]
                label = dimensions[currentId]["category"]["index"][]
                print("\t", label)

if __name__ == "__main__":
    # getAllAsFile("PEA07")
    getFormated("PEA07")
    
        
    