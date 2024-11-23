import kagglehub

# Download latest version
path = kagglehub.dataset_download("simshengxue/league-of-legends-tribunal-chatlogs")

print("Path to dataset files:", path)