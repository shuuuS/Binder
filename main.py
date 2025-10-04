from os import scandir

from time import sleep
import logging

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from setup import *
from functions.nameFiles import *
from functions.moveFiles import *

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
                self.check_exe_files(entry, name)

    def check_video_files(self, entry, name):  
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(video_dir, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_document_files(self, entry, name):  
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(document_dir, entry, name)
                logging.info(f"Moved document/pdf file: {name}")

    def check_image_files(self, entry, name): 
        for img_extension in image_extensions:
            if name.endswith(img_extension) or name.endswith(img_extension.upper()):
                move_file(image_dir, entry, name)
                logging.info(f"Moved img file: {name}")

    def check_zip_files(self, entry, name): 
        for zip_extension in zip_extensions:
            if name.endswith(zip_extension) or name.endswith(zip_extension.upper()):
                move_file(zip_dir, entry, name)
                logging.info(f"Moved zip/rar file: {name}")

    def check_exe_files(self, entry, name): 
        for exe_extension in exe_extensions:
            if name.endswith(exe_extension) or name.endswith(exe_extension.upper()):
                move_file(exe_dir, entry, name)
                logging.info(f"Moved exe file: {name}")


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
