import os

# Directory containing the files you want to rename
directory = r"C:\Users\theod\Pictures\zTest4"

# Function to list files in batches
def batch_files(directory, batch_size=100):
    files = os.listdir(directory)
    for i in range(0, len(files), batch_size):
        yield files[i:i+batch_size]

# Iterate through files in batches
for batch in batch_files(directory):
    for filename in batch:
        if os.path.isfile(os.path.join(directory, filename)):
            # Split the filename into name and extension
            name, ext = os.path.splitext(filename)

            # Check if the extension is empty or not .png
            if ext == "" or ext != ".png":
                # Rename the file with a .png extension
                new_filename = name + ".png"
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f"Renamed: {filename} to {new_filename}")
