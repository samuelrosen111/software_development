#!/bin/bash


echo "List all files and folders in the current directory recursively"

# Define a function to list files and folders recursively
list_files_and_folders() {
  local current_dir="$1"

  # Iterate over items in the current directory
  for item in "$current_dir"/*; do
    # Check if the item is a directory
    if [ -d "$item" ]; then
      # Print the directory name and its contents
      echo "Directory: <$(basename "$item")>"
      list_files_and_folders "$item"  # Recursively list contents
    elif [ -f "$item" ]; then
      # Print the file name
      echo "\t $(basename "$item")"
    fi
  done
}

# Start listing from the current directory
list_files_and_folders "$(pwd)"
