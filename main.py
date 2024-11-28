import os
import re

def to_pascal_case(name):
    """Convert a string to PascalCase."""
    base_name, ext = os.path.splitext(name)
    words = re.split(r'[\s_\-]+', base_name)  # Handles spaces, underscores, and hyphens
    pascal_case_name = ''.join(word.capitalize() for word in words if word)
    return pascal_case_name + ext  # Reattach the original file extension

def rename_files_to_pascal_case(root_directory):
    """Rename all files in a directory and its subdirectories to PascalCase."""
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            old_path = os.path.join(dirpath, filename)
            new_filename = to_pascal_case(filename)
            new_path = os.path.join(dirpath, new_filename)
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f'Renamed: "{old_path}" -> "{new_path}"')

def main():
    """Main application loop to prompt for input."""
    print("Welcome to the PascalCase Renamer!")
    while True:
        root_directory = input("Enter the directory path (or 'exit' to quit): ").strip()
        if root_directory.lower() == 'exit':
            print("Exiting the application. Goodbye!")
            break
        if not os.path.isdir(root_directory):
            print("Invalid directory. Please try again.")
        else:
            rename_files_to_pascal_case(root_directory)
            print("\nRenaming complete!\n")

if __name__ == "__main__":
    main()
