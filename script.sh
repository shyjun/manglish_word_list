#!/bin/bash

# Input file (passed as first argument)
input_file="words.txt"

# Output file (optional second argument, defaults to input_file.sorted.txt)
output_file="words_sorted.txt"

if [[ ! -f "$input_file" ]]; then
  echo "Error: Input file '$input_file' does not exist."
  exit 1
fi

# Process: sort and remove duplicates
sort "$input_file" | uniq > "$output_file"

echo "Sorted and unique words saved to: $output_file"
