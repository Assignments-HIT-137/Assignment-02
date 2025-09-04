import os
def create_raw_text_file(filename="raw_text.txt"):
    """
    Creates a sample text file for the program to use.
    """
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("This is a test file for the encryption program.\n")
            f.write("12345 Hello World! ABCDEFGHIJKLMNOPQRSTUVWXYZ\n")
            f.write("This is a simple message for testing.")
        print(f"Created sample file: {filename}")
def decrypt_file(shift1, shift2, input_filename="encrypted_text.txt", output_filename="decrypted_text.txt"):
    """
    Decrypts the content of a file based on the original encryption rules.
    Reads from input_filename and writes to output_filename.
    """
    try:
        with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
            content = infile.read()
            decrypted_content = ""
            for char in content:
                # Handle lowercase letters
                if 'a' <= char <= 'z':
                    # Decryption is the reverse of encryption
                    # First half (a-m) encryption was forward shift1*shift2, so decryption is backward
                    # Second half (n-z) encryption was backward shift1+shift2, so decryption is forward
                    if 'a' <= char <= 'm':
                        base = ord('a')
                        offset = ord(char) - base  
                        shift = (shift1 * shift2) % 13
                        decrypted_content += chr(base + (offset - shift) % 13)
                    else: # n-z
                        base = ord('n')
                        offset = ord(char) - base  
                        shift = (shift1 + shift2) % 13
                        decrypted_content += chr(base + (offset + shift) % 13)

                # Handle uppercase letters
                elif 'A' <= char <= 'Z':
                    # Decryption is the reverse of encryption
                    if 'A' <= char <= 'M':
                        base = ord('A')
                        offset = ord(char) - base  
                        shift = shift1 % 13
                        decrypted_content += chr(base + (offset + shift) % 13)
                    else: # N-Z
                        # Encryption was forward shift2**2, so decryption is backward
                        base = ord('N')
                        offset = ord(char) - base  
                        shift = (shift2 ** 2) % 13
                        decrypted_content += chr(base + (offset - shift) % 13)
                
                # Handle all other characters
                else:
                    decrypted_content += char
            outfile.write(decrypted_content)
        print(f"File '{input_filename}' decrypted successfully to '{output_filename}'.")
        return True
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return False
def encrypt_file(shift1, shift2, input_filename="raw_text.txt", output_filename="encrypted_text.txt"):
    """
    Encrypts the content of a file based on the given shift values and rules.
    Reads from input_filename and writes to output_filename.
    """
    try:
        with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
            content = infile.read()
            encrypted_content = ""
            for char in content:
                # Handle lowercase letters
                if 'a' <= char <= 'z':
                    # Handle a-m letters
                    if 'a' <= char <= 'm':
                        # First half: shift forward by shift1 * shift2
                        base = ord('a')
                        offset = ord(char) - base  
                        shift = (shift1 * shift2) % 13 # using modulus 13 to ensure that the shift stays within the 13 letters
                        encrypted_content += chr(base + (offset + shift) % 13) # %13 to wrap around oif it goes past 'm'
                    else: # n-z
                        # Second half: shift backward by shift1 + shift2
                        base = ord('n')
                        offset = ord(char) - base  
                        shift = (shift1 + shift2) % 13
                        encrypted_content += chr(base + (offset - shift) % 13)

                # Handle uppercase letters
                elif 'A' <= char <= 'Z':
                    if 'A' <= char <= 'M':
                        base = ord('A')
                        offset = ord(char) - base  
                        shift = shift1 % 13
                        encrypted_content += chr(base + (offset - shift) % 13)
                    else: # N-Z
                        # Second half: shift forward by shift2 squared
                        base = ord('N')
                        offset = ord(char) - base  
                        shift = (shift2 ** 2) % 13
                        encrypted_content += chr(base + (offset + shift) % 13)

                # Handle all other characters
                else:
                    encrypted_content += char
            outfile.write(encrypted_content)
        print(f"File '{input_filename}' encrypted successfully to '{output_filename}'.")
        return True
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return False

def main():
    """
    Main function to run the entire encryption, decryption, and verification process.
    """
    create_raw_text_file()

    try:
        input1 = (input("Please enter the first shift value (shift1): "))
        shift1 = int(input1)
    except ValueError:
        if type(input1)== str:
            ascii_sum =sum((ord(ch)for ch in input1))
            shift1= ascii_sum % 13
            print(f"using {shift1} as shift1 ")
        else:
            print("Invalid input.")
            return
        
    try:

        input2 = input("Please enter the second shift value (shift2): ")
        shift2= int(input2)
    except ValueError:

        if type(input2)== str:
            ascii_sum =sum((ord(ch)for ch in input2))
            shift2= ascii_sum % 13
            print(f"using {shift2} as shift2 ")
        else:
            print("Invalid input. Please enter integer values.")
            return

    # Encrypt the file
    if encrypt_file(shift1, shift2):
        # Decrypt the file
        if decrypt_file(shift1, shift2):
            # Verify the result
            verify_decryption()

if __name__ == "__main__":
    main()