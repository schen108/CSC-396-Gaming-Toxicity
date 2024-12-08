import subprocess

command = ["pip3", "install", "kagglehub"]
result = subprocess.run(command, capture_output=True, text=True)


import kagglehub


github = "/home/jovyan/data-store/CSC-396-Gaming-Toxicity"

# Dota dataset
path = kagglehub.dataset_download("danielfesalbon/gosu-ai-english-dota-chat")
print("Path to Dota dataset files:", path)

command = ["mv", path, github]
result = subprocess.run(command, capture_output=True, text=True)
print(f"Moved files from {path} to {github}")

print(result.stdout)

if result.stderr:
    print("Errors:")
    print(result.stderr)


path = kagglehub.dataset_download("simshengxue/league-of-legends-tribunal-chatlogs")
print("Path to League dataset files:", path)

command = ["mv", path, github]
result = subprocess.run(command, capture_output=True, text=True)
print(f"Moved files from {path} to {github}")

print(result.stdout)

if result.stderr:
    print("Errors:")
    print(result.stderr)


# Kaggle chats
path = kagglehub.dataset_download("saurabhshahane/cyberbullying-dataset")
print("Path to dataset files:", path)

command = ["mv", path, github]
result = subprocess.run(command, capture_output=True, text=True)
print(f"Moved files from {path} to {github}")

print(result.stdout)

if result.stderr:
    print("Errors:")
    print(result.stderr)