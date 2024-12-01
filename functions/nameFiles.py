from os.path import splitext, exists

# Handle name files 
def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name