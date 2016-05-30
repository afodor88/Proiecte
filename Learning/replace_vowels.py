def anti_vowel(text):
    vowels = 'aeiou'
    for character in text:
        for vowel in vowels:
            if character.lower() == vowel:
                text = text.replace(character, '')
    return text

text = 'Hello Python'

print anti_vowel(text)