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