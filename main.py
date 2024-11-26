def count_characters(text:str=None):
    text = text.lower()
    # Add it to the dictionary that you will return
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # filter out spaces, and special characters, including, exclamation marks
    for char in [' ', '\n', '\t', '\r', '!', '.', ',', '?', ';', ':', '"', "'", "%", "$", "&", "*", "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "+", "-", "_", "=", "@", "#"]:
        if char in char_count:
            del char_count[char]

    # filter out numbers
    for char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if char in char_count:
            del char_count[char]

    return char_count

def count_words(text:str=None):
    words = text.split()
    return len(words)

def main():
    path_to_file = "books/frankenstein.txt"
    num_words = 0
    char_count = {}

    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        char_count = count_characters(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times.")
    print("--- End report ---")

if __name__ == '__main__':
    main()