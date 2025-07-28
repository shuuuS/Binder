# Binder
The program sorts files with the appropriate extensions.

# How to use it?
## First step
You must edit file named 'setup.py' and add your paths and folders:
```python
# PATHS TO FOLDERS
source_dir = "PATH_TO_DOWNLOAD_FOLDER"
zips_dir = "PATH_TO_FOLDER_WITH_SPECIFIC_EXTENSION"
images_dir = "PATH_TO_FOLDER_WITH_SPECIFIC_EXTENSION"
docs_dir = "PATH_TO_FOLDER_WITH_SPECIFIC_EXTENSION"
video_dir = "PATH_TO_FOLDER_WITH_SPECIFIC_EXTENSION"
exe_dir = "PATH_TO_FOLDER_WITH_SPECIFIC_EXTENSION"

# supported image types
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

# supported document types
document_extensions = [".doc", ".docx", ".odt", ".xls", ".xlsx", ".txt", ".pdf"]

# supported zip\rar types
zip_extensions = ['.rar', ".zip"]

# supported video types
video_extensions = [".mp4", ".mov", ".mp3"]

# supported exe types
exe_extensions = [".exe"]
```
Remember: i included only the most common supported file types for extensions (if you need, u can add more).
## Second step
Remember to start from file named 'main.py' and download supported python libraries from requirements.txt

# How program works?
Normally program will works when you start python script (main.py).
I suggest to add that file to startup folder (for windows: Press the Windows key + R to open the Run dialog and
Type shell:startup)

## Example usage
<img width="462" height="70" alt="image" src="https://github.com/user-attachments/assets/c9d3a59c-a383-4506-aa25-c23dc17125be" />

