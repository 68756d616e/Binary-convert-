# Welcome to the first version of the binary to text converter! 

binary_string = input("Enter an 8-bit binary string: ") # Convert the string input!

# Convert from binary to text
convert = {
    '0': 'a',
    '1': 'b',
    '00': 'c',
    '11': 'd',
    '000': 'e',
    '111': 'f',
    '0000': 'e',
    '1111': 'f',
    '00000': 'a',
    '11111': 'b',
    '000000': 'c',
    '111111': 'd',
    '0000000': 'e',
    '1111111': 'f',
    '00000000': 'e',
    '11111111': 'f'
}

# Convert the binary string to text using the convert!
text = ""
i = 0
while i < len(binary_string):
    if i == len(binary_string) - 1:  # Last digit of binary string
        text += convert[binary_string[i]]
        break
    if binary_string[i:i+2] in convert:  # Two-digit binary code
        text += convert[binary_string[i:i+2]]
        i += 2
    elif binary_string[i:i+3] in convert:  # Three-digit binary code
        text += convert[binary_string[i:i+3]]
        i += 3
    elif binary_string[i:i+4] in convert:  # Four-digit binary code
        text += convert[binary_string[i:i+4]]
        i += 4
    elif binary_string[i:i+5] in convert:  # Five-digit binary code
        text += convert[binary_string[i:i+5]]
        i += 5
    elif binary_string[i:i+6] in convert:  # Six-digit binary code
        text += convert[binary_string[i:i+6]]
        i += 6
    elif binary_string[i:i+7] in convert:  # Seven-digit binary code
        text += convert[binary_string[i:i+7]]
        i += 7
    else:  # Single-digit binary code
        text += convert[binary_string[i]]
        i += 1

print("The text representation is:", text)
