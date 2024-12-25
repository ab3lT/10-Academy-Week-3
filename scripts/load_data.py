import os
import zipfile
import io



def extract_zip(zip_file_path: str, extract_to: str) -> None:
    """
    Extracts a zip file to the specified directory.

    Args:
        zip_file_path (str): The path to the zip file.
        extract_to (str): The directory where the zip contents will be extracted.
    """
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
       
def extract_nested_zip(outer_zip_path: str, extract_to: str) -> None:
    with zipfile.ZipFile(outer_zip_path, 'r') as outer_zip:
        for file_info in outer_zip.infolist():
            if file_info.filename.endswith(".zip"):
                
                with outer_zip.open(file_info.filename) as nested_zip_file:
                    nested_zip_data = io.BytesIO(nested_zip_file.read())
                    with zipfile.ZipFile(nested_zip_data, 'r') as nested_zip:
                        nested_zip.extractall(extract_to)
            else:
                outer_zip.extract(file_info, extract_to)
        
    