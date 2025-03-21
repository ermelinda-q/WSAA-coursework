from github import Github
from config import config as cfg 

apikey = cfg["githubkey"]

g = Github(apikey)

repo = g.get_repo("https://github.com/ermelinda-q/aprivateone")
print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url

print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.txt 

print(contentOfFile)

newContents = contentOfFile + " more stuff \n"
print(newContents)

gitHubResponse = repo.update_file(fileInfo.path, "updated by prog", newContents, fileInfo.sha)
print(gitHubResponse)

