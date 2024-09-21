This Python script performs a backup of a specified folder and ensures that files that have already been backed up are not duplicated. The script is ideal for users who want to back up important directories to another location while avoiding redundant copies of unchanged files.

Features
Backup Entire Folder: Backs up all contents of a specified folder, including subdirectories.
Avoid Redundant Copies: Skips copying files that have already been backed up.
Date-Based Backup Naming: Appends the current date to the backup folder name for easy tracking of backup versions.
Automatic Directory Creation: If the backup directory does not exist, the script automatically creates it.
Prerequisites
Ensure you have the following prerequisites installed before running the script:

Python 3.x
The following Python modules (which are part of the standard library):
shutil
os
datetime
How to Use
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/folder-backup-utility.git
cd folder-backup-utility
Modify the Script: You can modify the source and destination paths in the script directly or pass them as arguments to the take_backup function.

Run the Script: Make sure Python is installed on your system. To run the backup script, open a terminal and execute the following command:

bash
Copy code
python backup.py
Example Usage: The following example backs up a folder named Certificates located on your desktop to a Backup folder, also on your desktop. It checks if any files have already been backed up to avoid duplicates.

python
Copy code
take_backup(
    src_folder_name="Certificates",
    src_dir="C:/Users/Admin/OneDrive - Auckland Institute of Studies/Desktop",
    dst_dir="C:/Users/Admin/OneDrive - Auckland Institute of Studies/Desktop/Backup"
)
Parameters:
src_folder_name: The name of the folder you want to back up (e.g., Certificates).
src_dir: The directory path where the source folder is located.
dst_dir: The directory path where the backup should be saved. The script will create a new subdirectory with today's date to store the backup files.
How the Script Works
Source and Destination Paths:

The script first constructs the source path from the provided directory and folder name.
It constructs the destination path and appends the current date to the folder name, creating a unique backup folder.
File Copying:

The script recursively traverses through the source folder, preserving its folder structure in the backup location.
For each file, it checks if a copy already exists in the backup folder. If the file is already backed up, it skips the file to prevent redundancy.
Output:

The script prints a message for each file it copies, as well as for files that it skips because they already exist in the destination folder.

