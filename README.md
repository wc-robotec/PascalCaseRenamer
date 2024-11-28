# Pascal Case Renamer

A Python script that renames all files in a directory and its subdirectories to **PascalCase** (UpperCamelCase).

## Requirements
- python 3.XX

## Features
- Recursively processes files in all subdirectories.
- Converts filenames from various formats (snake_case, kebab-case, etc.) to PascalCase.
- Handles spaces, hyphens, and underscores automatically.

---
## How to use - Linux (Ubuntu/Debian)
### (Optional) Install python:
  ```bash
  sudo apt update && sudo apt upgrade # Update the package list
  sudo apt install python3 # Install Python (if not already installed)
  ```
### Clone repository
```bash
git clone https://github.com/wc-robotec/PascalCaseRenamer.git
cd PascalCaseRenamer
```

### Run script
```bash
python3 main.py <path-to-your-directory>
```
Output should be:
```python3
Welcome to the PascalCase Renamer!
Enter the directory path (or 'exit' to quit): /home/user/files
Renamed: "/home/user/files/my_file.txt" -> "/home/user/files/MyFile.txt"
Renamed: "/home/user/files/another_file-name.pdf" -> "/home/user/files/AnotherFileName.pdf"

Renaming complete!

Enter the directory path (or 'exit' to quit): exit
Exiting the application. Goodbye!
```

## How it works - example

### Before:
```
my_folder/
├── my_file.txt
├── another-file.pdf
└── sub_folder/
    └── test file.docx
```

### After:
```
my_folder/
├── MyFile.txt
├── AnotherFile.pdf
└── sub_folder/
    └── TestFile.docx
```

## Disclaimer

Ensure you have a backup of your files before running the script, as file renaming is irreversible.

---

## License

This project is licensed under the terms of the [MIT License](LICENSE).
