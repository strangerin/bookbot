def count_words(text):
    return len(text.split())


def count_letters(text):
    count_letters = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in count_letters:
                count_letters[char_lower] += 1
            else:
                count_letters[char_lower] = 1
    return count_letters
