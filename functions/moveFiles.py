from shutil import move
from os.path import exists, join
from os import rename

from functions.nameFiles import make_unique

# Function for transport files
def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)
