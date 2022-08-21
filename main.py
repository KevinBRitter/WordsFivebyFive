# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def load_words():
    with open('Word Lists/2022_words.json') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    print_hi('PyCharm')
    english_words = load_words()
    # demo print
    print('fate' in english_words)
    print(english_words)
