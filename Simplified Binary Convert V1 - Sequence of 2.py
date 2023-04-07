# Simplified Binary Convert V1 - Sequence of 2 - It has no name yet!
# about

# It started as 
    # '00': 'a',
    # '11': 'b',
    # '000': 'c', # Not included 
    # '111': 'd', # Not included 
    # '0000': 'e', # Not included 
    # '1111': 'f', # Not included 

# The above is segments of 4 incomplete! I wanted to show as it was before I completed it!
# The below was created to simplify it into segments of 2, orginially it was segments of 8! The additional version will be in 8 as a minimum
# # Take input from the user
# binary_input = input("Enter a binary number: ")
# # Separate the input into segments of two
# segments = [binary_input[i:i+2] for i in range(0, len(binary_input), 2)]

while True:
    # The user inputs a binary sequence
    binary_input = input("Enter a binary number (or 'quit' to exit): ") # At the moment it has not been limited to a particular amount

    # If the users would like to quit! 
    if binary_input.lower() == "quit":
        break

    # The seperation of the inputted sequence divided into segments of 2
    segments = [binary_input[i:i+2] for i in range(0, len(binary_input), 2)] # This is an alteration of version 1

    # Convert each segment into the provided format! 
    converted_segments = [] # Set to null
    for segment in segments:
        if segment == "01":
            converted_segments.append("01")
        elif segment == "10":
            converted_segments.append("10")
        elif segment == "00":
            converted_segments.append("a")
        elif segment == "11":
            converted_segments.append("b")

    # The converted segments joined
    result = " ".join(converted_segments)
    print(result)

# The issues above consist of the user input 000 or 111 as an example, there are many other issues :)
# I will correct it in the other version!
