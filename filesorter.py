import os, shutil

path = r"C:/Users/sidd_/Documents/AUTOMATIC_FILE_SORTER/"  # Directory path
file_names = os.listdir(path)                               # List all files in the directory

folder_names = ["xlsx files", "txt files", "jpg files"]     # Folder names for sorting

# Create folders if they don't exist
for folder in folder_names:
    if not os.path.exists(path + folder):                   
        os.makedirs(path + folder)                           # Create folder

# Loop through each file and move to respective folder
for file in file_names:
    if ".xlsx" in file and not os.path.exists(path + "xlsx files/" + file):
        shutil.move(path + file, path + "xlsx files/")      # Move Excel files
    elif ".jpg" in file and not os.path.exists(path + "jpg files/" + file):
        shutil.move(path + file, path + "jpg files/")       # Move JPEG images
    elif ".txt" in file and not os.path.exists(path + "txt files/" + file):
        shutil.move(path + file, path + "txt files/")       # Move text files
