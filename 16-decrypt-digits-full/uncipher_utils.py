

all_characters = [ "a", "b", "c", "d", "e", "f", "g" ]

def get_one_absent_character(charlist):
    for char in all_characters:
        if char not in charlist:
            return char
            break

def cipher_ready(cipher):
    #print("Checking cipher data: %s" %cipher[-4:])
    for item in cipher[-4:]:
        if item.known == False:
            return False
    else:
        return True

def get_data(cipher, after):
    value = ''
    for item in cipher[-4:]:
        #print("Summing digit: %s" %item)
        value += str(item.unciphered)

    #print("Unciphered: %s" %cipher)
    print("Value: %s (after %s)" %(value, after))
    return int(value)

