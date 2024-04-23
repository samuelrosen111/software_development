#!/bin/bash

# List all .cs files in the current directory
cs_files=$(find . -maxdepth 1 -type f -name "*.cs")

# Check if any .cs files were found
if [ -z "$cs_files" ]; then
    echo "No C# files found in the current directory."
    exit 1
fi

# Display the list of C# files with numbers
echo "Select a C# program to compile and run:"
select cs_file in $cs_files; do
    if [ -n "$cs_file" ]; then
        break
    else
        echo "Invalid selection. Please try again."
    fi
done

# Extract the file name without extension
file_name=$(basename -s .cs "$cs_file")

# Compile the C# program
mcs "$cs_file" -out:"$file_name.exe"

# Check if compilation was successful
if [ $? -ne 0 ]; then
    echo "Compilation failed."
    exit 1
fi

# Run the compiled program using mono
echo "Running $file_name.exe ..."
mono "$file_name.exe"

# Remove the compiled .exe file
rm "$file_name.exe"
echo "$file_name.exe has been removed after running."
