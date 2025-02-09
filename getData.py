import kagglehub



def fetch_dataset():
    # Download latest version
    path = kagglehub.dataset_download("thomaskonstantin/3500-popular-creepypastas")

    return path