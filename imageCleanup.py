import os
import shutil

def move_jpeg_files(source_folder, destination_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    # Check if the destination folder exists, and create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List all files in the source folder
    files = os.listdir(source_folder)

    # Iterate through the files and move .jpeg files to the destination folder
    for file in files:
        if file.lower().endswith((".jpeg", ".png")):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            try:
                shutil.move(source_path, destination_path)
                print(f"Moved '{file}' to '{destination_folder}'.")
            except Exception as e:
                print(f"Error moving '{file}': {str(e)}")

# Example usage:
source_folder = "/Users/laurasolis/desktop"
destination_folder = "/Users/laurasolis/desktop/imagesJunk"

move_jpeg_files(source_folder, destination_folder)
