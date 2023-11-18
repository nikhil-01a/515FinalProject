import sys


def count_lines_words_char(text):
    lines = text.split('\n')
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = len(text)
    return num_lines, num_words, num_chars


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"Error: {filename} not found!")
    else:
        text = sys.stdin.read()

    numlines, numwords, numchars = count_lines_words_char(text)
    print(f"{numlines:8d} {numwords:7d} {numchars:7d} {filename if len(sys.argv)==2 else ''}")
