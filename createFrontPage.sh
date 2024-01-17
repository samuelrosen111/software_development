#!/bin/bash

# Script to create an HTML file listing files and folders in the current directory

echo "Creating an HTML file to list files and folders separately..."

# Define the HTML file name
html_file="front_page.html"

# Function to convert a path to a 'file://' URL on Unix-like systems
path_to_url() {
  echo "file://$(realpath "$1" | sed 's|/|\/|g')"
}

# Function to read README.md and convert it to HTML
add_readme() {
  if [ -f "README.md" ]; then
    echo "<div style='background-color: blue; color: white; padding: 10px; margin-bottom: 20px;'>" >> "$html_file"
    echo "<p> README.md file content: </p>" >> "$html_file"
    while IFS= read -r line || [[ -n "$line" ]]; do
      echo "<p>$line</p>" >> "$html_file"
    done < "README.md"
    echo "</div>" >> "$html_file"
  fi
}

# Start the HTML file content
echo "<html><head><title>Directory Structure</title></head><body>" > "$html_file"

# Add README contents if available
add_readme

# Heading for the directory structure
echo "<h1>Directory Structure of $(pwd)</h1>" >> "$html_file"
echo "<style>body { font-family: Arial, sans-serif; } .file-box, .folder-box { padding: 10px; margin-bottom: 20px; } .file-box { background-color: lightgreen; } .folder-box { background-color: orchid; }</style>" >> "$html_file"

# Function to list files in the current directory
list_files() {
  local current_dir="$1"

  echo "<div class='file-box'>" >> "$html_file"
  echo "<h2>Files</h2>" >> "$html_file"
  echo "<ul>" >> "$html_file"

  # Iterate over items in the current directory to find files
  for item in "$current_dir"/*; do
    if [ -f "$item" ]; then
      # Print the file name
      echo "<li>$(basename "$item")</li>" >> "$html_file"
    fi
  done

  echo "</ul>" >> "$html_file"
  echo "</div>" >> "$html_file"
}

# Function to list folders in the current directory
list_folders() {
  local current_dir="$1"

  echo "<div class='folder-box'>" >> "$html_file"
  echo "<h2>Folders</h2>" >> "$html_file"
  echo "<ul>" >> "$html_file"

  # Iterate over items in the current directory to find folders
  for item in "$current_dir"/*; do
    if [ -d "$item" ]; then
      # Print the directory name with a clickable link
      local dir_url=$(path_to_url "$item")
      echo "<li>Directory: <a href='$dir_url'>$(basename "$item")</a></li>" >> "$html_file"
    fi
  done

  echo "</ul>" >> "$html_file"
  echo "</div>" >> "$html_file"
}

# List files and folders
list_files "$(pwd)"
list_folders "$(pwd)"

# Finish the HTML file
echo "</body></html>" >> "$html_file"

echo "HTML file 'front_page.html' has been created."
