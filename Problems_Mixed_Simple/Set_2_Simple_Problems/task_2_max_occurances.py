def maximumOccurringCharacter(text):
    used_letters = []
    max_letter = None
    max_letter_count = 0
    for letter in text:
        if letter not in used_letters:
            used_letters.append(letter)
            letter_count = text.count(letter)
            if letter_count > max_letter_count:
                max_letter = letter
                max_letter_count = letter_count

    print(max_letter)


maximumOccurringCharacter('helloworld')
