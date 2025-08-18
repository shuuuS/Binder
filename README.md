# Binder
Binder is a lightweight background script designed to automatically organize your downloaded files based on their extensions. Ideal for users who want a cleaner, more structured "Downloads" folder without manual sorting
# Features
* Runs silently in the background (recommended to launch at system startup)
* Monitors a user-defined folder (typically the "Downloads" folder)
* Automatically sorts files into pre-configured folders based on file extensions
* Fully customizable: set your own scan folder, destination folders, and extension rules
# How to use it?
!! Program doesn't work like as .exe file, so you must follow below instructions
## For download, try use below git command:
```python
git clone https://github.com/shuuuS/Binder.git
```
Include download needed library from requirements.txt
## On first run, configure:
* The folder to monitor (e.g. Downloads)
* Destination folders for each file type
* Which extra extensions should be handled by which folder

Configuration is done in a file called setup.py:
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
Remember: i included only the most common supported file types for extensions (if you need, u can add more)

# Usage
Before make it working silently in background, check your setups manually by running script and download random file (e.g. cat image from google photos :D)

## Example usage
<img width="462" height="70" alt="image" src="https://github.com/user-attachments/assets/c9d3a59c-a383-4506-aa25-c23dc17125be" />

# How to set the script to run at system startup?
It can be done by many ways but i will tell only about one of them:
For windows:
1) Press the Windows key + R to open the Run dialog and Type shell:startup)
2) Make there new text file - Binder.txt and copy/paste below code:
```python
@echo off
cd /d "PATH_TO_FOLDER_WITH_PROGRAM"
start /min "" "PATH_TO_FOLDER_WITH_PROGRAM\.venv\Scripts\pythonw.exe" "PATH_TO_FOLDER_WITH_PROGRAM\main.py"
```
3) Name Binder.txt as Binder.bat

Now, if you restart your PC, program should launch when system windows start

# Author
Created by [Jakub Kwiatkowski](https://github.com/shuuuS)

