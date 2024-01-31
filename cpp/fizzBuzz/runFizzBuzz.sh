#!/bin/bash

# Ask the user for three integer inputs
echo "Enter three integers separated by spaces (e.g., 2 3 7):"
read a b n

# Compile fizzBuzz.cpp
g++ fizzBuzz.cpp -o fizzBuzz

./fizzBuzz $a $b $n

