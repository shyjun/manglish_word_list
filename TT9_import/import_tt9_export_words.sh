#!/bin/bash

set -x

cut -f1 TT9_import/words.csv | sort | uniq > my_words.txt

