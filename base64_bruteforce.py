import base64  # Import the base64 module to perform Base64 encoding and decoding

def decode_base64(encoded_string, times):
    decoded_string = encoded_string  # Initialize the decoded string with the encoded input
    for _ in range(times):  # Loop for the specified number of decoding times
        try:
            # Pad the string if its length is not a multiple of 4
            while len(decoded_string) % 4 != 0:
                decoded_string += '='  # Add padding character '=' to make the length a multiple of 4
            
            decoded_bytes = base64.b64decode(decoded_string)  # Decode the Base64 string into bytes
            decoded_string = decoded_bytes.decode('utf-8')  # Decode bytes to a UTF-8 string
            print(f"Decoded string: {decoded_string}")  # Print the decoded string
        except Exception as e:
            print(f"Error during decoding: {e}")  # Print any errors that occur during decoding
            break  # Exit the loop if there's an error

def main():
    # Use a list to store each line of input
    encoded_lines = []  
    print("Enter Base64 encoded string (type 'end' to finish):")  # Prompt the user for input
    
    while True:
        line = input()  # Read a line of input from the user
        if line.lower() == 'end':  # Check if the user typed 'end' to finish input
            break  # Exit the loop
        encoded_lines.append(line)  # Save each line to the list

    # Combine the lines into a single string and remove newlines
    encoded_string = ''.join(encoded_lines)

    # Input the number of times to decode
    while True:
        try:
            times = int(input("Enter the number of times to decode: "))  # Prompt for number of decodes
            if times < 1:  # Check if the number is less than 1
                raise ValueError("Number of times must be greater than 0.")  # Raise an error
            break  # Exit the loop if valid input is received
        except ValueError as ve:
            print(ve)  # Print the error message for invalid input

    # Perform decoding
    decode_base64(encoded_string, times)  # Call the decode function with the string and number of times

if __name__ == "__main__":
    main()  # Call the main function if the script is executed
