from functools import lru_cache

# Mapping letters to encrypted form
codes = {
    'A': '._',   'B': '_...', 'C': '_._.', 'D': '_..',  'E': '.',
    'F': '.._.', 'G': '__.',  'H': '....', 'I': '..',   'J': '.___',
    'K': '_._',  'L': '._..', 'M': '__',   'N': '_.',   'O': '___',
    'P': '.__.', 'Q': '__._', 'R': '._.',  'S': '...',  'T': '_',
    'U': '.._',  'V': '..._', 'W': '.__',  'X': '_.._',
    'Y': '_.__', 'Z': '__..'
}

# Reverse map
decode_map = {}
for ch, pattern in codes.items():
    if pattern not in decode_map:
        decode_map[pattern] = []
    decode_map[pattern].append(ch)

encrypted = input().strip()
max_len = max(len(p) for p in decode_map)

@lru_cache(None)
def solve(pos):
    if pos == len(encrypted):
        return [""]

    words = []
    for length in range(1, max_len + 1):
        part = encrypted[pos:pos + length]
        if part in decode_map:
            for letter in decode_map[part]:
                for tail in solve(pos + length):
                    words.append(letter + tail)
    return words

result = solve(0)

for w in sorted(result):
    print(w)
