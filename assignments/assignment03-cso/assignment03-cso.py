# Web Services and Application (WSAA)
# Assignment 3 - Reading apis in the wild (Topic 4)
# Author: E. Qejvani

######## Task ########

# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO.
# Store the dataset into a file called "cso.json".
# Upload this program to the same repository you used for the first assignment.
# Save this assignment as "assignment03-cso.py".

import requests
import json

url_begining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
url_ending = "/JSON-stat/2.0/en"
def get_all_as_file(dataset):
    with open("exchequer_acc_cso.json", "wt") as fp:
        print(json.dumps(get_all_data(dataset)), file=fp)
        
def get_all_data(dataset):
    url = url_begining + dataset + url_ending
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    get_all_as_file("FIQ02")
    