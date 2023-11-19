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
        description='Count lines, words, and characters in text files.')
    parser.add_argument('-l', '--lines', action='store_true',
                        help='Count only lines')
    parser.add_argument('-w', '--words', action='store_true',
                        help='Count only words')
    parser.add_argument('-c', '--chars', action='store_true',
                        help='Count only characters')
    parser.add_argument('filenames', nargs='*', type=argparse.FileType('r'),
                        default=[sys.stdin], help='File(s) to read from (stdin if not provided)')
    args = parser.parse_args()

    total_lines, total_words, total_chars = 0, 0, 0
    for file in args.filenames:
        try:
            text = file.read()
            numlines, numwords, numchars = count_lines_words_char(text)

            if not (args.lines or args.words or args.chars):
                args.lines, args.words, args.chars = True, True, True

            output = []
            if args.lines:
                output.append(f"{numlines:8d}")
            if args.words:
                output.append(f"{numwords:7d}")
            if args.chars:
                output.append(f"{numchars:7d}")
            output.append(f"{file.name if file is not sys.stdin else ''}")
            print(" ".join(output))

            total_lines += numlines
            total_words += numwords
            total_chars += numchars
        except FileNotFoundError:
            print(f"Error: {file.name} not found!")
            sys.exit(1)
        finally:
            if file is not sys.stdin:
                file.close()

    if len(args.filenames) > 1 and args.filenames[0] is not sys.stdin:
        total_output = []
        if args.lines:
            total_output.append(f"{total_lines:8d}")
        if args.words:
            total_output.append(f"{total_words:7d}")
        if args.chars:
            total_output.append(f"{total_chars:7d}")
        total_output.append("total")
        print(" ".join(total_output))

    sys.exit(0)


if __name__ == "__main__":
    main()
