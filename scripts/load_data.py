import os
import zipfile



def extract_zip(zip_file_path: str, extract_to: str) -> None:
    """
    Extracts a zip file to the specified directory.

    Args:
        zip_file_path (str): The path to the zip file.
        extract_to (str): The directory where the zip contents will be extracted.
    """
    with zipfile,zipfile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        