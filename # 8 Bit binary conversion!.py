# 8 Bit binary conversion! 

# Welcome message 
print("Welcome to 8 Binary conversion, please choose an option!")

while True:
        
    # 8 Bit Binary variations
    binaryvariations = {}
    for i in range(256):
        binary = format(i, '08b') # convert the integer to an 8-bit binary string
        binaryvariations[binary] = i # add the binary string to the variations dictionary

    initial_question = input("""Please choose one of the following.
    A - Info about 8 Bit binary!
    B - Binary Converter
    Type either A or B : """)

    if initial_question == 'A' or initial_question == 'a':
        print("8 bit etc")
        question_followup = input("Would you like all the8 Bit binary variations!")
        
        if question_followup == 'yes' or question_followup == 'YES':
            print(binaryvariations)
            secondary_question = input("Would you like to use the binary conveter, yes or exit? :")

            if secondary_question == "yes":
                
                # Define the variations
                variations = {
                    "00": "a",
                    "11": "b",
                    "00000000": "c",
                    "11111111": "d",
                    "0000" : "e",
                    "1111": "f",
                    "000" : "g",
                    "111" : "h",
                    "0" : "0",
                    "1" : "1"
                }
                        
                # Take input from the user
                binary_input = input("Enter an 8-bit binary number: ")

                # Separate the input into segments of 2
                segments = [binary_input[i:i+2] for i in range(0, len(binary_input), 2)]

                # Convert each segment into one of the predefined variations
                converted_segments = []
                for segment in segments:
                    if segment in variations:
                        converted_segments.append(variations[segment])
                    else:
                        converted_segments.append(segment)

                # Join the converted segments and print the result
                result = "".join(converted_segments)

                # Divide the output into 8 segments
                output_segments = [result[i:i+8] for i in range(0, len(result), 8)]

                # Check if there is a remainder
                remainder = len(result) % 8

                # Print the output segments
                if remainder == 0:
                    print(" ".join(output_segments))
                else:
                    print(" ".join(output_segments[:-1]), output_segments[-1])  # Output all but the last segment with a space separator and output the last segment without a space separator

            
            elif secondary_question == "exit":
                print(initial_question)

            else:
                print("Please type in lower either exit or yes")
            
    elif initial_question == "b" or initial_question == "B":

        # Define the variations
        variations = {
            "00": "a",
            "11": "b",
            "00000000": "c",
            "11111111": "d",
            "0000" : "e",
            "1111": "f",
            "000" : "g",
            "111" : "h",
            "0" : "0",
            "1" : "1"
        }
                
        # Take input from the user
        binary_input = input("Enter an 8-bit binary number: ")

        # Separate the input into segments of 2
        segments = [binary_input[i:i+2] for i in range(0, len(binary_input), 2)]

        # Convert each segment into one of the predefined variations
        converted_segments = []
        for segment in segments:
            if segment in variations:
                converted_segments.append(variations[segment])
            else:
                converted_segments.append(segment)

        # Join the converted segments and print the result
        result = "".join(converted_segments)

        # Divide the output into 8 segments
        output_segments = [result[i:i+8] for i in range(0, len(result), 8)]

        # Check if there is a remainder
        remainder = len(result) % 8

        # Print the output segments
        if remainder == 0:
            print(" ".join(output_segments))
        else:
            print(" ".join(output_segments[:-1]), output_segments[-1])  # Output all but the last segment with a space separator and output the last segment without a space separator
