import os
import zipfile

# Get the current working directory
base_directory = os.getcwd()

# Specify the destination folder where you want to extract the contents
destination_folder = "audio/"

# Iterate through the file names from "001.zip" to "114.zip"
for i in range(1, 115):
    file_name = f"{i:03d}.zip"  # Format the file name with leading zeros if needed

    # Construct the complete path to each ZIP file
    zip_file_path = os.path.join(base_directory, file_name)

    # Check if the file exists before attempting to extract it
    if os.path.exists(zip_file_path):
        # Create a ZipFile object and extract the contents
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(destination_folder)
        print(f"Extracted {file_name} to {destination_folder}")
    else:
        print(f"Skipping {file_name} as it does not exist.")
