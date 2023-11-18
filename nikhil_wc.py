def count_lines_words_char(text):
    lines = text.split('\n')
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = len(text)
    return num_lines, num_words, num_chars
