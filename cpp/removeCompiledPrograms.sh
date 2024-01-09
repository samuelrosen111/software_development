#!/bin/bash

# Get the current directory
current_dir=$(pwd)

# List all files that are not .cpp or .sh files
files_to_remove=$(find "$current_dir" -type f ! -name "*.cpp" ! -name "*.sh")

# Check if there are any files to remove
if [ -z "$files_to_remove" ]; then
  echo "No files found in the current directory that are not .cpp or .sh files."
  exit 0
fi

# Display the list of files to remove
echo "Files found in the current directory that are not .cpp or .sh files:"
echo "$files_to_remove"
echo

# Ask the user if they want to remove these files
read -p "Do you want to remove these files? (yes/no): " choice

case "$choice" in
  yes|YES|y|Y)
    # Remove the files
    echo "Removing files..."
    rm -f $files_to_remove
    echo "Files removed."
    ;;
  no|NO|n|N)
    echo "No files were removed."
    ;;
  *)
    echo "Invalid choice. No action taken."
    ;;
esac

exit 0
