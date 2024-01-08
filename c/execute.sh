#!/bin/bash

# Check if gcc (GNU C compiler) is available
if ! command -v gcc &> /dev/null; then
    echo "Error: gcc (GNU C compiler) is not installed or not in your PATH."
    exit 1
fi

# Check if walkthrough.c exists in the current directory
if [ ! -f "walkthrough.c" ]; then
    echo "Error: 'walkthrough.c' file not found in the current directory."
    exit 1
fi

# Compile the C program and create an executable named 'walkthrough'
gcc -o walkthrough walkthrough.c

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful. Running 'walkthrough'..."
    ./walkthrough
else
    echo "Compilation failed."
fi