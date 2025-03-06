# Web Services and Application (WSAA)
# Assignment 3 - Reading apis in the wild (Topic 4)
# Author: E. Qejvani

######## Task ########

# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO.
# Store the dataset into a file called "cso.json".
# Upload this program to the same repository you used for the first assignment.
# Save this assignment as "assignment03-cso.py".

# Importing the modules/libraries.
import requests
import json

# I am dividing the url in three parts - based on topic 4 video lesson by A. Beaty.

base_url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
format_details = "/JSON-stat/2.0/en"
dataset_id = "FIQ02"

# Getting data from the API and saving it to 'cso.json'.
def get_all_as_file(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(get_all_data(dataset)), file=fp)
        
# Getting data from the API for the given dataset ID.
def get_all_data(dataset):
    url = base_url + dataset+ format_details
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    get_all_as_file(dataset_id)
    