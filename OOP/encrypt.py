

alphabet = ['a', 'b', 'c', 'ə']

def encrypt(text):
    return ''.join([
        alphabet[(alphabet.index(text[i])+1) if alphabet.index(text[i]) < len(alphabet) - 1 else 0]
        for i in range(len(text))
    ])

print(encrypt('ab'))
print(encrypt('cə'))
