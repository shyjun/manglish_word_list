#!/bin/bash

set -x

# Input file (passed as first argument)
input_file="my_words.txt"

# Output file (optional second argument, defaults to input_file.sorted.txt)
output_file="my_words_sorted.txt"

if [[ ! -f "$input_file" ]]; then
  echo "Error: Input file '$input_file' does not exist."
  exit 1
fi

# Process: sort and remove duplicates
sort "$input_file" | uniq > "$output_file"

echo "Sorted and unique words saved to: $output_file"

# get global malayalam dictionary words
sed '1d' dictionaries/ml_wordlist.combined |  cut -d '=' -f 2 | cut -d ',' -f 1 > dict_words.txt

# convert to english
python3 tools/ml_2_en.py dict_words.txt dict_words_converted.txt

# create words.txt
cat dict_words_converted.txt my_words_sorted.txt | grep -v '^$' | sort | uniq > words.txt

