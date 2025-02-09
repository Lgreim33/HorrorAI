import kagglehub

# Download latest version
path = kagglehub.dataset_download("thomaskonstantin/3500-popular-creepypastas")

print("Path to dataset files:", path)