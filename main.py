from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep
import logging

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# PATHS TO FOLDERS
source_dir = "C:/Users/Kuba/Downloads"
zips_dir = "C:/Users/Kuba/Downloads/ZIPY"
images_dir = "C:/Users/Kuba/Downloads/IMAGES"
docs_dir = "C:/Users/Kuba/Downloads/PDF"
video_dir = "C:/Users/Kuba/Downloads/WIDEO"

# supported image types
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

# supported document types
document_extensions = [".doc", ".docx", ".odt", ".xls", ".xlsx", ".txt", ".pdf"]

# supported zip/rar types
zip_extensions = ['.rar', ".zip"]

# supported video types
video_extensions = [".mp4", ".mov"]

# Handle name files 
def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

# Function for transport files
def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

# Main function
class ChooseDirectory(FileSystemEventHandler):
    def on_modified(self, event):
        # Scan folder
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_document_files(entry, name)
                self.check_image_files(entry, name)
                self.check_zip_files(entry, name)
                self.check_video_files(entry, name)

    def check_video_files(self, entry, name):  # Checks all Video Files
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(video_dir, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_document_files(self, entry, name):  # Checks all Document Files
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(docs_dir, entry, name)
                logging.info(f"Moved document/pdf file: {name}")

    def check_image_files(self, entry, name): # Check all Image Files
        for img_extension in image_extensions:
            if name.endswith(img_extension) or name.endswith(img_extension.upper()):
                move_file(images_dir, entry, name)
                logging.info(f"Moved img file: {name}")

    def check_zip_files(self, entry, name): # Check all Zip/rar files
        for zip_extension in zip_extensions:
            if name.endswith(zip_extension) or name.endswith(zip_extension.upper()):
                move_file(zips_dir, entry, name)
                logging.info(f"Moved zip/rar file: {name}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = ChooseDirectory()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()