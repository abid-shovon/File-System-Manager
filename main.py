import os
import sys

def check_current_dicrectory():
    print("Current directory is:", os.getcwd())

    
def show_files():
    all_files = os.listdir()
    for files in all_files:
        print(files)

def create_single_folder():
    try:
        folder_name = input("Enter the folder name: ")
        os.mkdir(folder_name)
    except Exception as e:
        print("SomeThing is wrong", e)
    
def create_nested_folders():
    root_folder_name = input("Enter the Root file-name: ")
    current_path = root_folder_name
    
    os.makedirs(current_path, exist_ok=True)
    print(f"Root Folder is: {current_path}")
    
    while True:
        try:
            choice = input("Do you want to create a sub-folder inside this? (y|n): ").strip().lower()
            if choice in ["yes", "ye", "y"]:
                sub_folder = input("Enter the name of the next sub-folder: ").strip()
                current_path = os.path.join(current_path, sub_folder)
                os.makedirs(current_path, exist_ok=True)
                print(f"Created folder: {current_path}")
            elif choice in ["no", "n"]:
                print("--------------Exit---------------")
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
        
        except ValueError as e:
            print("SomeThing is wrong", e)
    
    print(f"Nested Folder path is: {current_path}")

def text_file():
    try:
        name = input("Enter file name (ex:help.txt): ").strip()
        with open(name, "a") as data:
            data.write(input(">>> ") + "\n")
    except Exception as e:
        print("SomeThing is wrong", e)
    
def rename_folder_or_file_name():
    show_files()
    choice = input("Enter the file or folder name which you want to rename: ")
    if os.path.exists(choice):
        new_name = input("Enter new name of your file: ")
        os.rename(choice, new_name)
    else:
        print("File not found.")

def remove_single_folder():
    show_files()
    try:
        choice = input("Write the filename which you want to delete: ")
        if not os.path.exists(choice):
            print("File not found")
        else: 
            confirm = input("Confirm to delete (Y|N): ").lower()
            if confirm in ["yes", "y"]:
                os.rmdir(choice)
                print(f"{choice} is deleted. ")
            else:
                print("Cancel the deleting process.")
    except ValueError as e:
        print("SomeTing is wrong.", e)

def remove_file():
    show_files()
    try:
        choice = input("Write the filename which you want to delete: ")
        if not os.path.exists(choice):
            print("File not found")
        else: 
            confirm = input("Confirm to delete (Y|N): ").lower()
            if confirm in ["yes", "y"]:
                os.remove(choice)
                print(f"{choice} is deleted. ")
            else:
                print("Cancel the deleting process.")
    except ValueError as e:
        print("SomeTing is wrong.", e)

def check_file():
    choice = input("Write the filename: ")
    if os.path.exists(choice):
        print("Yes the file is exist in current directory.")
    else:
        print("File not found in current directory")

def exit_programe():
    print("Exiting program. Goodbye!")
    sys.exit()
        
      
def main_menu():
    operation = {
    1: check_current_dicrectory,
    2: show_files,
    3: create_single_folder,
    4: create_nested_folders,
    5: text_file,
    6: rename_folder_or_file_name,
    7: remove_single_folder,
    8: remove_file,
    9: check_file,
    0: exit_programe         
    }
    
    while True:
        print('''
        ====== File System Manager ======
        1. Check current directory
        2. List all files and folders
        3. Create single folder
        4. Create nested folders
        5. Create .txt file
        6. Rename folder or file
        7. Remove a directory
        8. Remove a file
        9. Check if a file exists
        0. Exit
        ''')
        try:
            user_input = int(input("Choice which you want: "))
            action = operation.get(user_input)
            if action:
                action()
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Please enter a valid number.") 
               
        restart = input("Do ou want to restart (Y|N) >>> ").lower()
        if restart not in ["yes", "ye", "y"]:
            exit_programe()
        else:
            continue
        

if __name__ == "__main__":
    main_menu()