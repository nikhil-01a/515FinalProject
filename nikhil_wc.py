import sys
import argparse


def count_lines_words_char(text):
    lines = text.split('\n')
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = len(text)
    return num_lines, num_words, num_chars


def main():
    parser = argparse.ArgumentParser(
        description='Count lines, words, and characters in a text file.')
    parser.add_argument('filename', nargs='?', type=argparse.FileType(
        'r'), default=sys.stdin, help='File to read from (stdin if not provided)')
    args = parser.parse_args()

    try:
        text = args.filename.read()
    except FileNotFoundError:
        print(f"Error: {args.filename.name} not found!")
        sys.exit(1)

    numlines, numwords, numchars = count_lines_words_char(text)
    print(f"{numlines:8d} {numwords:7d} {numchars:7d} {args.filename.name if args.filename is not sys.stdin else ''}")

    args.filename.close()
    sys.exit(0)


if __name__ == "__main__":
    main()
