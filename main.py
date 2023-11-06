import requests

base_url = "https://everyayah.com/data/Alafasy_128kbps/zips/"

# Iterate through the file names from "001.zip" to "114.zip"
for i in range(1, 115):
    file_name = f"{i:03d}.zip"  # Format the file name with leading zeros if needed

    # Construct the complete URL for each file
    file_url = base_url + file_name

    # Send an HTTP GET request to download the file
    response = requests.get(file_url)

    if response.status_code == 200:
        # If the request was successful, save the file to your local directory
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {file_name}")
