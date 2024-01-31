#!/bin/bash

# Initialize an empty array to hold all program names
declare -a programs

# Function to list C programs and add them to the programs array
list_c_programs() {
    echo "C programs:"
    echo "--------------------------------------------------------"
    local i=1
    for file in *.c; do
        if [ -f "$file" ]; then
            echo "$i) $file"
            programs+=("$file")
            ((i++))
        fi
    done
}

# Function to list C++ programs and add them to the programs array
list_cpp_programs() {
    echo "C++ programs:"
    echo "--------------------------------------------------------"
    for file in *.cpp; do
        if [ -f "$file" ]; then
            # Correctly calculate and display the enumeration
            echo "$((${#programs[@]} + 1))) $file"
            programs+=("$file")
        fi
    done
}

# List all C and C++ programs
list_c_programs
list_cpp_programs

# Ask the user to pick a program to run
echo "Enter the number of the program you want to run: "
read choice

# Validate the user input
if ! [[ "$choice" =~ ^[0-9]+$ ]] || [ "$choice" -lt 1 ] || [ "$choice" -gt "${#programs[@]}" ]; then
    echo "Error: Please enter a valid number between 1 and ${#programs[@]}."
    exit 1
fi

# Use the choice to get the selected program from the array
selected_program=${programs[$choice-1]}

# Determine the file extension to select the compiler
extension="${selected_program##*.}"

# Compile the selected program
if [ "$extension" = "c" ]; then
    gcc "$selected_program" -o program
elif [ "$extension" = "cpp" ]; then
    g++ -std=c++11 "$selected_program" -o program
else
    echo "Error: Unsupported file type."
    exit 1
fi

# Check if compilation was successful
if [ $? -ne 0 ]; then
    echo "Error: Compilation failed."
    exit 1
fi

# Run the compiled program
./program

# Remove the compiled executable after execution
rm -f program

echo "Program executed and compiled file removed."
