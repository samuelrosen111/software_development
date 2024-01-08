#!/bin/bash

# Simple start
echo "Hello World"

# Example variables
greeting="Hello"
name="User"

echo "$greeting $name"

# Read user input for name
read -p "Enter your name: " name
echo "Hello $name, nice to meet you!"

# Read user input for number
echo "Please enter a number: "
read number

# Check if the number is even or odd
if (( number % 2 == 0 ))
then
    echo "The number $number is even"
else
    echo "The number $number is odd"
fi

# Counting with a for-loop
echo "Now let's use a for-loop to count. Enter the number you want to count to: "
read count

# Convert negative number to positive
if [ $count -lt 0 ]
then
    echo "You entered a negative number ($count). Converting to positive..."
    count=$((count * -1))
    echo "The number is now $count"
fi

for (( i=1; i<=$count; i++ ))
do
    echo $i
done

# Counting with a while-loop
echo "Now let's use a while-loop to count. Enter the number you want to count to: "
read while_count 

#convert negative number to positive
if [ $while_count -lt 0 ]
then
    echo "You entered a negative number ($while_count). Converting to positive..."
    while_count=$((while_count * -1))
    echo "The number is now $while_count"
fi

index=1

while [ $index -le $while_count ]
do
    echo $index
    index=$((index + 1))
done

