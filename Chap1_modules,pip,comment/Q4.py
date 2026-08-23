import os  # os module gives access to operating system functionality like reading directories

# ask the user to enter a directory path
path = input("D:\Python_Series ")

try:
    # attempt to get the list of files/folders in the given path
    contents = os.listdir(path)
    
    print(f"Contents of '{path}':")
    
    # print each file/folder name on its own line
    for item in contents:
        print(item)

except FileNotFoundError:
    # runs if the given path does not exist
    print("Directory not found.")

except PermissionError:
    # runs if the program lacks permission to read the directory
    print("Permission denied.")