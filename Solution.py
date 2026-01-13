# dictionary for letters and their encrypted codes
code = {
    'A': '._',   'B': '_...', 'C': '_._.', 'D': '_..',
    'E': '.',    'F': '.._.', 'G': '__.',  'H': '....',
    'I': '..',   'J': '.___', 'K': '_._',  'L': '._..',
    'M': '__',   'N': '_.',   'O': '___',  'P': '.__.',
    'Q': '__._', 'R': '._.',  'S': '...',  'T': '_',
    'U': '.._',  'V': '..._', 'W': '.__',  'X': '_.._',
    'Y': '_.__', 'Z': '__..'
}

# reverse dictionary so we can go from code to the letter
reverse_code = {}
for letter in code:
    value = code[letter]
    if value not in reverse_code:
        reverse_code[value] = []
    reverse_code[value].append(letter)

# list to store all the answers
answers = []

# recursive function 
def solve(encrypted, index, current_word):
    # if we reached end of string, store the answer
    if index == len(encrypted):
        answers.append(current_word)
        return

    
    for c in reverse_code:
        length = len(c)

        # check if code matches starting from index
        if encrypted[index:index + length] == c:
            for letter in reverse_code[c]:
                # move forward and add letter
                solve(encrypted, index + length, current_word + letter)

# take input
encrypted_message = input().strip()

# call brute force solver
solve(encrypted_message, 0, "")

# print answers in alphabetical order
answers.sort()
for word in answers:
    print(word)
