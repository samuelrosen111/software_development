#!/bin/bash

# List all C files and numerate them
echo "Available C programs:"
files=(*.c)
for i in "${!files[@]}"; do
    echo "$((i+1))) ${files[i]}"
done

# Ask the user to choose a program to compile
echo "Enter the number of the program you want to compile and run:"
read -r choice

# Validate the user input
if ! [[ "$choice" =~ ^[0-9]+$ ]] || [ "$choice" -lt 1 ] || [ "$choice" -gt "${#files[@]}" ]; then
    echo "Invalid selection."
    exit 1
fi

# Compile the selected program
selected_file="${files[$((choice-1))]}"
exe_name="${selected_file%.*}"  # Remove the .c extension to use as executable name

# Use gcc to compile the C program
if gcc "$selected_file" -o "$exe_name"; then
    echo "Compilation successful. Running $exe_name ..."

    # Execute the compiled program
    ./"$exe_name"

    # Remove the compiled executable after execution
    echo "Removing executable..."
    rm -f "$exe_name"
else
    echo "Compilation failed."
fi
