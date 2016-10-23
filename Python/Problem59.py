def get_text():
    FILENAME = 'p059_cipher.txt'
    with open(FILENAME, 'r') as file:
        file = file.readline()
    file = file.split(',')
    file = [int(s) for s in file]
    return file


def to_human(text):
    text = [str(chr(s)) for s in text]
    return text


def calc_freq(human_text):
    count = sum(1 for s in human_text if s.lower() == 'e')
    return count/len(human_text)


def apply_key(text, key):
    key = [ord(s) for s in key]
    decrypted_text = [0] * len(text)
    for i in range(0, len(text), 3): 
        decrypted_text[i] = text[i] ^ key[0]
        if i+1 < len(text):
            decrypted_text[i+1] = text[i+1] ^ key[1]
        if i+2 < len(text):
            decrypted_text[i+2] = text[i+2] ^ key[2]
    return decrypted_text


def key_gen():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                yield ''.join([a, b, c])


if __name__ == '__main__':
    text = get_text()
    for key in key_gen(): 
        decrypted_text = apply_key(text, key)
        human_text = to_human(decrypted_text)
        if calc_freq(human_text) > 0.10:
            print(sum(decrypted_text))
            print(human_text)

