import os
import fnmatch
import zipfile

def extract_zip(zip_file_path, destination_folder):
    # Create a new folder path based on the zip file name
    new_folder_name = os.path.splitext(os.path.basename(zip_file_path))[0]
    new_folder_path = os.path.join(destination_folder, new_folder_name)

    # Create the new folder
    os.makedirs(new_folder_path, exist_ok=True)

    # Extract the zip file contents to the new folder
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(new_folder_path)
    
    # Remove the zip file
    os.remove(zip_file_path)

    print(f"Extracted '{zip_file_path}' to '{new_folder_path}'")

def find_zip_files(directory):
    zip_files = []
    # Iterate through the directory
    for dirpath, dirnames, filenames in os.walk(directory):
        # if the file name ends in .zip
        for filename in fnmatch.filter(filenames, '*.zip'):
            # recreate the path and add it to the zip_files array
            zip_file_path = os.path.join(dirpath, filename)
            zip_files.append(zip_file_path)
    # return all zip files
    return zip_files

def main():
    folder_path = r'C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomLevels'

    # figures out whether the songs are on the C drive or not, only accepting Y or N
    choice = 'a'
    while choice != "Y" and choice != "N":
        choice = input("Is your Beatsaber on your C drive? (Y/N)\n").upper()

    # if saved in a different drive
    if choice == "N":
        driveLetter = 'a'
        if len(driveLetter) != 1:
            driveLetter = input("Enter the letter of your drive: ").upper()
        
        # sets the new folder path
        folder_path = driveLetter+':\SteamLibrary\steamapps\common\Beat Saber\Beat Saber_Data\CustomLevels'

    # extract the songs in the folder
    zip_files = find_zip_files(folder_path)
    for file in zip_files:
        extract_zip(file, folder_path)

if '__main__' == __name__:
    main()