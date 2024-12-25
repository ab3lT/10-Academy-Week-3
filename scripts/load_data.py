import os
import zipfile



def extract_zip(zip_file_path: str, extract_to: str) -> None:
    
    with zipfile,zipfile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        