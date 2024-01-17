#!/bin/bash

echo "This script will calculate the first 100 primes and write them to a file."

# Helper function to calculate if a number is prime
is_prime() {
    local number=$1
    local sqrt_number=$(echo "sqrt($number)" | bc)

    if (( number < 2 )); then
        echo "false"
        return
    fi

    if (( number == 2 || number == 3 )); then
        echo "true"
        return
    fi

    if (( number % 2 == 0 || number % 3 == 0 )); then
        echo "false"
        return
    fi

    # Check from 5 to the square root of the number
    for (( i=5; i<=sqrt_number; i+=2 )); do
        if (( number % i == 0 )); then
            echo "false"
            return
        fi
    done

    echo "true"
}

# Function to create the prime array
create_prime_list() {
    local primes_array=(2 3)
    local current_number=4

    while [ ${#primes_array[@]} -lt 100 ]; do
        if [[ $(is_prime $current_number) == "true" ]]; then
            primes_array+=($current_number)
        fi
        ((current_number++))
    done

    echo "${primes_array[@]}"
}

main() {
    # Create prime array
    primes_array=( $(create_prime_list) )

    # File name
    local file_name="prime_numbers.txt"
    local file_content="This file contains the first 100 prime numbers:\n"

    # Add each prime number to the file content
    for prime in "${primes_array[@]}"; do
        file_content+="$prime\n"
    done

    # Write to the file
    echo -e "$file_content" > "$file_name"

    echo "File '$file_name' created with the first 100 prime numbers."
    echo "End of script."
}

# Call the main function
main
