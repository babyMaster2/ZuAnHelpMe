import re
if __name__ == '__main__':

    with open('src/quotes/test_quotes.txt', 'r+', encoding='utf-8') as f:
        lines = [line for line in f.readlines() if line != '\n']

    pattern = re.compile(r'\b(?:[1-9]|[1-9][0-9]|100)\b、')
    new_lines = [pattern.sub('', line) for line in lines]
    with open('src/quotes/test_quotes.txt', 'w+', encoding='utf-8') as f:
        f.writelines(new_lines)
