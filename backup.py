import shutil
from datetime import date
import os

# Function for performing the backup of folders and ensuring no duplicate backup
def take_backup(src_folder_name, dst_folder_name=None, src_dir='', dst_dir=''):
    try:
        # Extract today's date for backup naming convention
        today = date.today()
        date_format = today.strftime("%d_%b_%Y_")

        # Construct the full source and destination paths
        src_dir = os.path.join(src_dir, src_folder_name)
        dst_dir = os.path.join(dst_dir, dst_folder_name if dst_folder_name else src_folder_name)

        # Check if source directory exists
        if not os.path.isdir(src_dir):
            print(f"Source folder '{src_dir}' does not exist.")
            return

        # Append date to destination directory to make the backup folder unique
        dst_dir = os.path.join(dst_dir, date_format + src_folder_name)

        # Ensure the destination directory exists, create if necessary
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        # Loop through all files and subdirectories in the source directory
        for root, dirs, files in os.walk(src_dir):
            # Get relative path to mirror directory structure in backup folder
            relative_path = os.path.relpath(root, src_dir)
            backup_subdir = os.path.join(dst_dir, relative_path)

            # Create subdirectories in destination, if they don't already exist
            if not os.path.exists(backup_subdir):
                os.makedirs(backup_subdir)

            # Copy each file if it doesn't already exist in the destination
            for file_name in files:
                src_file_path = os.path.join(root, file_name)
                dst_file_path = os.path.join(backup_subdir, file_name)

                # Check if the file already exists in the destination
                if not os.path.exists(dst_file_path):
                    shutil.copy2(src_file_path, dst_file_path)
                    print(f"Copied: {src_file_path} -> {dst_file_path}")
                else:
                    print(f"Skipped (already backed up): {dst_file_path}")

        print("Backup Completed Successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Call the function to backup the 'Certificates' folder
take_backup(
    src_folder_name="Certificates",
    src_dir="C:/Users/Admin/OneDrive - Auckland Institute of Studies/Desktop",
    dst_dir="C:/Users/Admin/OneDrive - Auckland Institute of Studies/Desktop/Backup"
)
