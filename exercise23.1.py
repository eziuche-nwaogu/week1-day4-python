# This is an improvement on exercise 23 where a user is required to enter the name of the fie to be decoded
import sys

script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)


text_file = input("Enter the name of the file you wish to decode: ")
languages = open(text_file, encoding="utf-8")

main(languages, input_encoding, error)
