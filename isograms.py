def is_isogram(string):
    unique_letters = []
    letters = [letter.lower() for letter in list(string)]
    for letter in letters:
        if letter not in unique_letters and not letter.isnumeric():
            unique_letters.append(letter)
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    assert is_isogram("Dermatoglyphics") is True
    assert is_isogram("MIGUEL") is True
    assert is_isogram("Lunatic") is True
    assert is_isogram("jOhN") is True
    assert is_isogram("ABCDEFGHIJKLMNOPQRSTUVWXYZ") is True
    assert is_isogram("") is True

    assert is_isogram("aba") is False
    assert is_isogram("mo0se") is False
    assert is_isogram("Robert") is False
    assert is_isogram("r41nF4ll") is False
    assert is_isogram("ABCDEFGHIJKLMNOPQRSTUVWXYZA") is False
