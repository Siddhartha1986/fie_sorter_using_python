
# Simple File Sorter Using Python

## Introduction
This repository contains a Python script for a simple file sorter utility. The script automates the organization of files in a specified directory, sorting them into designated folders based on their file extensions. It utilizes Python's `os` and `shutil` libraries to interact with the file system.

## Features
- **Automated File Sorting**: Automatically sorts files into folders based on file types.
- **Customizable**: Easily adaptable for different file types and directory paths.
- **User-Friendly**: Simple and straightforward to use, even for those with basic knowledge of Python.

## Prerequisites
- Python 3.x installed on your system.
- Basic understanding of Python scripting and file directories.

## How to Use
1. **Clone the Repository**: 
   ```
   git clone https://github.com/Siddhartha1986/file_sorter_using_python.git
   ```
2. **Customize the Script**: 
   - Open the script in your preferred text editor or IDE.
   - Modify the `path` variable to the directory you want to sort.
   - Adjust `folder_names` to match the types of files you want to organize.
3. **Run the Script**: 
   - Navigate to the script directory in your command line or terminal.
   - Run the script using Python:
     ```
     python file_sorter.py
     ```

## Usage Example
Suppose you have a directory mixed with `.txt`, `.jpg`, and `.xlsx` files. Running this script will automatically create three folders named "txt files", "jpg files", and "xlsx files" (if they don't already exist) and move each file into its corresponding folder based on its extension.

## Contributing
Contributions to this project are welcome. Feel free to fork the repository, make improvements, and submit a pull request. If you have any suggestions or encounter any issues, please post them in the issues section of this repository.


