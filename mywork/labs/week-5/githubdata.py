import requests
import json
from config import config as cfg 

filename = "github-private-repo.json"
apiKey = cfg["githubkey"]

url = "https://api.github.com/repos/ermelinda-q/aprivateone"

response = requests.get(url, auth=("token", apiKey))

print(response.status_code)

repoJSON = response.json()
with open(filename, "w") as fp:
    json.dump(repoJSON, fp, indent=4)
    
