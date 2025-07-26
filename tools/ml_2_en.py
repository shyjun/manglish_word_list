import sys
import os
import re
import string

# Add local ml2en/ directory to module path
local_ml2en_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ml2en"))
sys.path.insert(0, local_ml2en_path)

from ml2en import ml2en

def clean(text):
    # Step 1: Remove unwanted characters (ZWNJ, ZWJ, ^, $)
    text = re.sub(r'[\u200c\u200d\^\$]', '', text)

    # Step 2: Remove ASCII control characters (like \x01, \x00)
    text = ''.join(ch for ch in text if ch in string.printable and ord(ch) >= 32)

    # Step 3: Convert to lowercase
    return text.lower()

def usage():
    print("Usage: python ml_2_en.py <input.txt> <output.txt>")
    sys.exit(1)

def main():
    if len(sys.argv) != 3:
        usage()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        converter = ml2en()

        with open(input_file, "r", encoding="utf-8") as f:
            malayalam_words = [line.strip() for line in f if line.strip()]

        english_words = [
            clean(converter.transliterate(word)) for word in malayalam_words
        ]

        with open(output_file, "w", encoding="utf-8") as f:
            for word in english_words:
                f.write(word + "\n")

        print(f"Transliteration complete. Output written to '{output_file}'")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
