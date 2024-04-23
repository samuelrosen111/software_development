#!/bin/bash

# This is a comment

# Print "hello world" to the terminal
echo "hello world"

print_example_variables(){
    string_var="Hello, world!"
    int_var=5
    float_var=2.2
    bool_var=true
    vector_var=(1 2 3 4 5)
    vectory_var2=(1 "hello" 3 "world" 5)

    # Print out all variables
    echo "Printing some example variables: "
    echo $string_var $int_var $float_var $bool_var $vector_var $vectory_var2
}

calculate_primes() {
    primes=(2 3 5 7)
    current_number=8
    for index in {1..100}; do
        is_prime=1
        for prime in "${primes[@]}"; do
            if [ $((current_number % prime)) -eq 0 ]; then
                is_prime=0
                break
            fi
        done
        if [ $is_prime -eq 1 ]; then
            primes+=($current_number)
        fi
        current_number=$((current_number + 1))
    done

    # Finally print out the primes
    echo "The first 100 primes are: "
    echo "${primes[@]}"
}

loops_walkthrough(){
    # While loop
    i=0
    while [ $i -lt 10 ]; do
        echo "While loop iteration: $i"
        i=$((i + 1))
        # Sleep for 0.5 seconds
        sleep 0.1
    done
}

print_bash(){
    echo ""
    # Define each letter pattern as an array of strings
    declare -a B=("BBBBBBB"
                "B     B"
                "BBBBBBB"
                "B     B"
                "BBBBBBB")

    declare -a A=(" AAAAA "
                "A     A"
                "AAAAAAA"
                "A     A"
                "A     A")

    declare -a S=(" SSSSS "
                "S      "
                " SSSSS "
                "      S"
                " SSSSS ")

    declare -a H=("H     H"
                "H     H"
                "HHHHHHH"
                "H     H"
                "H     H")

    # Print each letter
    for row in {0..4}; do
        echo "${B[$row]} ${A[$row]} ${S[$row]} ${H[$row]}"
    done
    echo ""
}


print_example_variables
calculate_primes
loops_walkthrough
print_bash
