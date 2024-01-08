#!/bin/bash

# Check if g++ (GNU C++ compiler) is available
if ! command -v g++ &> /dev/null; then
    echo "Error: g++ (GNU C++ compiler) is not installed or not in your PATH."
    exit 1
fi

# Check if walkthrough.cpp exists in the current directory
if [ ! -f "walkthrough.cpp" ]; then
    echo "Error: 'walkthrough.cpp' file not found in the current directory."
    exit 1
fi

# Compile the C++ program and create an executable named 'walkthrough'
g++ -o walkthrough walkthrough.cpp

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful. Running 'walkthrough'..."
    ./walkthrough
else
    echo "Compilation failed."
fi
