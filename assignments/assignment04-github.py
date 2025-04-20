# Web Services and Application (WSAA)
# Assignment 4 - Read and Edit a file from a repository.
# Author: E. Qejvani

######## Task ########
# Write a program in python that will read a file from a repository.
# The program should then replace all the instances of the text "Andrew" with your name. 
# The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).

# Importing modules.
from github import Github
import os
from config import config as cfg 

# 
apikey = cfg["githubkey"]
REPO_NAME = "ermelinda-q/WSAA-coursework"  # repo name
FILE_PATH = "assignments/data/text_to_change.txt"  # file to modify.

# Authenticate with GitHub
g = Github(apikey)
repo = g.get_repo(REPO_NAME)

# Get file contents
file = repo.get_contents(FILE_PATH)
file_content = file.decoded_content.decode("utf-8")

# Replacing "Andrew" with "Ermelinda"
updated_content = file_content.replace("Andrew", "Ermelinda")

# Append a new line after modification
modification_notice = "\nFile has been modified."
if not updated_content.endswith(modification_notice):
    updated_content += modification_notice

# Commit changes if there are modifications
if file_content != updated_content:
    repo.update_file(
        FILE_PATH,  # File path/File to modify.
        "Replaced 'Andrew' with 'Ermelinda' and added modification notice",  # Commit message
        updated_content,  # New content
        file.sha  # Required for update
    )
    print("File updated and changes pushed successfully.")
else:
    print("No changes needed.")


