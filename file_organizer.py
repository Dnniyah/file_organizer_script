import os  # Import the OS module to interact with the operating system
import shutil  # Import shutil for moving files

# Step 1: Get folder path from the user to organize
folder_to_organize = input("Enter the path of the folder you want to organize: ")

# Step 2: Define a dictionary that maps file extensions to folder names
extensions_to_folders = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.pdf': 'Documents',
    '.txt': 'Text Files',
    '.mp4': 'Videos',
    '.mp3': 'Audio',
    '.zip': 'Archives',
    '.docx': 'Documents',
}

# Step 3: Check if the folder exists
if os.path.exists(folder_to_organize):  # Check if the provided folder path exists
    try:
        # Step 4: Loop through all files in the folder
        for filename in os.listdir(folder_to_organize):  # List all files in the folder
            file_path = os.path.join(folder_to_organize, filename)  # Get the full file path

            # Step 5: Check if the item is a file, not a folder
            if os.path.isfile(file_path):
                # Step 6: Get the file extension (e.g., '.txt', '.jpg')
                file_extension = os.path.splitext(filename)[1]

                # Step 7: Look for the folder name in the dictionary, default to 'Other' if not found
                folder_name = extensions_to_folders.get(file_extension, 'Other')

                # Step 8: Create the folder path (e.g., '/path/to/Images/')
                folder_path = os.path.join(folder_to_organize, folder_name)

                # Step 9: If the folder doesn't exist, create it
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Step 10: Move the file to the appropriate folder
                shutil.move(file_path, folder_path)

                # Step 11: Notify the user that the file has been moved
                print(f"Moved {filename} to {folder_name}")
    except Exception as e:
        # Handle any unexpected errors during the process
        print(f"An error occurred: {e}")
else:
    # Step 12: If the folder doesn't exist, show an error message
    print(f"Error: The folder '{folder_to_organize}' does not exist.")
