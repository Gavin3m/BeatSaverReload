#$$$$$$\                       $$\      $$$$$$\            $$\                           $$$$$$$\            $$\                           $$\                         
#$  __$$\                      $$ |    $$  __$$\           $$ |                          $$  __$$\           $$ |                          $$ |                        
#$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\   $$ /  \__| $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$ |  $$ | $$$$$$\  $$ | $$$$$$\   $$$$$$\   $$$$$$$ |     $$$$$$\  $$\   $$\ 
#$$$$$$\ |$$  __$$\  \____$$\\_$$  _|  \$$$$$$\   \____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$$$$$$  |$$  __$$\ $$ |$$  __$$\  \____$$\ $$  __$$ |    $$  __$$\ $$ |  $$ |
#$  __$$\ $$$$$$$$ | $$$$$$$ | $$ |     \____$$\  $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|$$  __$$< $$$$$$$$ |$$ |$$ /  $$ | $$$$$$$ |$$ /  $$ |    $$ /  $$ |$$ |  $$ |
#$ |  $$ |$$   ____|$$  __$$ | $$ |$$\ $$\   $$ |$$  __$$ |$$ |  $$ |$$   ____|$$ |      $$ |  $$ |$$   ____|$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |    $$ |  $$ |$$ |  $$ |
#$$$$$$  |\$$$$$$$\ \$$$$$$$ | \$$$$  |\$$$$$$  |\$$$$$$$ |$$$$$$$  |\$$$$$$$\ $$ |      $$ |  $$ |\$$$$$$$\ $$ |\$$$$$$  |\$$$$$$$ |\$$$$$$$ |$$\ $$$$$$$  |\$$$$$$$ |
#_______/  \_______| \_______|  \____/  \______/  \_______|\_______/  \_______|\__|      \__|  \__| \_______|\__| \______/  \_______| \_______|\__|$$  ____/  \____$$ |
#                                                                                                                                                  $$ |      $$\   $$ |
#                                                                                                                                                  $$ |      \$$$$$$  |
#                                                                                                                                                  \__|       \______/ 

#----IMPORTS----#
import os
import fnmatch
import zipfile

#----Functions----#
def locateDrive():
    """Locates and returns the path of the CustomLevels directory."""
    # locate the drive using ASCII values from A to Z for windows-based drives
    for driveLetter in range(ord('A'), ord('Z') + 1):
            folder_path = chr(driveLetter)+r':\SteamLibrary\steamapps\common\Beat Saber\Beat Saber_Data\CustomLevels'
            if os.path.isdir(folder_path):
                return folder_path
    
    # locate the drive for Linux-based drives
    folder_path = os.path.expandvars('$HOME/.steam/steam/steamapps/common/Beat Saber/Beat Saber_Data/CustomLevels')
    if os.path.isdir(folder_path):
        return folder_path
    else:
        print("ERROR: folder not found")

def extract_zip(zip_file_path, destination_folder):
    """Creates a new directory in the destination folder and extracts data from the zip file into that new directory
    Parameters:
    zip_file_path (str): The path of the zip file 
    destination_folder (str): The path of the destination folder
   """
    # Create a new folder path based on the zip file name
    zip_file_name = os.path.basename(zip_file_path)
    # remove the extension
    new_folder_name = os.path.splitext(zip_file_name)[0]
    # create 
    new_folder_path = os.path.join(destination_folder, new_folder_name)

    # Create the new folder
    os.makedirs(new_folder_path, exist_ok=True)

    # Extract the zip file contents to the new folder
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(new_folder_path)
    
    # Remove the zip file
    os.remove(zip_file_path)

    # Print success message with to and from paths
    print(f"Extracted '{zip_file_path}' to '{new_folder_path}'")

def find_zip_files(directory):
    """Finds all of the zip files in a given directory
    Parameters:
    directory (str): path of the given directory
    Returns:
    str[]: each zip file path in the directory
   """
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
    """Main function that integrates everything"""
    folder_path = r'C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomLevels'
    # if that folder does not exist
    if not os.path.isdir(folder_path):
        # locate the CustomLevels folder
        folder_path = locateDrive()

    # find any zipped songs in the folder
    zip_files = find_zip_files(folder_path)
    
    # for each zipped song, unzip it
    for file in zip_files:
        extract_zip(file, folder_path)

#----Calling Main----#
if '__main__' == __name__:
    main()