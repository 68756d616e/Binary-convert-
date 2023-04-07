# Simplified Binary Convert V1 - Sequence of 4 - It has no name yet!
# Binary to text - specifically the alphabet

while True:
    # The user inputs a binary sequence
    binary_input = input("Enter a binary number (or 'quit' to exit): ") # At the moment it has not been limited to a particular amount

    # If the users would like to quit! 
    if binary_input.lower() == "quit":
        break

    # The seperation of the inputted sequence divided into segments of 2
    segments = [binary_input[i:i+4] for i in range(0, len(binary_input), 4)] # This is an alteration of version 1

    # Convert each segment into the provided format! 
    converted_segments = [] # Set to null
    for segment in segments:
        if segment == "01": # This will not show because of the sequence below! Unless its less than four
            converted_segments.append("01")
        elif segment == "10": # This will not show because of the sequence below!
            converted_segments.append("10")
        elif segment == "00": # This will not show because of the sequence below!
            converted_segments.append("a")
        elif segment == "11": # This will not show because of the sequence below!
            converted_segments.append("b")
        elif segment == "0000":
            converted_segments.append("c")
        elif segment == "0001":
            converted_segments.append("d")
        elif segment == "0010":
            converted_segments.append("e")
        elif segment == "0011":
            converted_segments.append("f")
        elif segment == "0100":
            converted_segments.append("g")
        elif segment == "0101":
            converted_segments.append("h")
        elif segment == "0110":
            converted_segments.append("i")
        elif segment == "0111":
            converted_segments.append("j")
        elif segment == "1000":
            converted_segments.append("k")
        elif segment == "1001":
            converted_segments.append("l")
        elif segment == "1010":
            converted_segments.append("m")
        elif segment == "1101":
            converted_segments.append("n")
        elif segment == "1110":
            converted_segments.append("o")
        elif segment == "1111":
            converted_segments.append("p")
        elif segment == "000": # Below is the less than 4 sequence
            converted_segments.append("q")
        elif segment == "001": 
            converted_segments.append("r")
        elif segment == "010":
            converted_segments.append("s")
        elif segment == "011":
            converted_segments.append("t")
        elif segment == "100":
            converted_segments.append("u")
        elif segment == "101":
            converted_segments.append("v")
        elif segment == "110":
            converted_segments.append("w")
        elif segment == "111":
            converted_segments.append("x")
        elif segment == "0": # Below is the less than 2 sequence - Just in case!
            converted_segments.append("0")
        elif segment == "1":
            converted_segments.append("1")

    # The converted segments joined
    result = " ".join(converted_segments) # With space
    result2 = "".join(converted_segments) # Without space

    # The printed result 
    print(result)
    print(result2)

