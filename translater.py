'''
vowels -> g
'''

def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter in "AEIOU":
                translation = translation + 'G'
            else:
                translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
