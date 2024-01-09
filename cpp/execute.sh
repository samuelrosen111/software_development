#!/bin/bash

# Find all .cpp files in the current directory
cpp_files=( *.cpp )

# Check if there are any .cpp files
if [ ${#cpp_files[@]} -eq 0 ]; then
    echo "No .cpp files found in the current directory."
    exit 1
fi

# Display a numbered list of .cpp files
echo "Select a C++ program to run:"
for ((i=0; i<${#cpp_files[@]}; i++)); do
    echo "$((i+1)): ${cpp_files[i]}"
done

# Ask the user to choose a file by number
read -p "Enter the number of the C++ program to run: " choice

# Validate the user's choice
if ! [[ "$choice" =~ ^[0-9]+$ ]] || ((choice < 1 || choice > ${#cpp_files[@]})); then
    echo "Invalid choice. Please enter a valid number."
    exit 1
fi

# Get the selected file
selected_file="${cpp_files[choice-1]}"

# Compile and run the selected C++ program
g++ "$selected_file" -o "${selected_file%.cpp}"
if [ $? -eq 0 ]; then
    echo "Compiling $selected_file..."
    "./${selected_file%.cpp}"
else
    echo "Compilation failed for $selected_file."
fi
