from functools import lru_cache

letter_to_code = {
    'A': '._',   'B': '_...', 'C': '_._.', 'D': '_..',  'E': '.',
    'F': '.._.', 'G': '__.',  'H': '....', 'I': '..',   'J': '.___',
    'K': '_._',  'L': '._..', 'M': '__',   'N': '_.',   'O': '___',
    'P': '.__.', 'Q': '__._', 'R': '._.',  'S': '...',  'T': '_',
    'U': '.._',  'V': '..._', 'W': '.__',  'X': '_.._',
    'Y': '_.__', 'Z': '__..'
}

code_to_letters = {}
for letter, code in letter_to_code.items():
    code_to_letters.setdefault(code, []).append(letter)

encrypted = input().strip()

@lru_cache(None)
def decode(index):
    if index == len(encrypted):
        return [""]

    result = []
    for code, letters in code_to_letters.items():
        if encrypted.startswith(code, index):
            for suffix in decode(index + len(code)):
                for letter in letters:
                    result.append(letter + suffix)
    return result

for word in sorted(decode(0)):
    print(word)
