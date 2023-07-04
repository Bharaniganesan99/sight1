# Reading a file in text mode
with open('text_file.txt', 'r') as file:
    content = file.read()
    print(content)  # Returns a string

# Reading a file in binary mode
with open('binary_file.bin', 'rb') as file:
    content = file.read()
    print(content)  # Returns bytes

# Writing to a file in text mode
with open('text_file.txt', 'w') as file:
    file.write('Hello, World!')

# Writing to a file in binary mode
with open('binary_file.bin', 'wb') as file:
    file.write(b'\x48\x65\x6C\x6C\x6F\x2C\x20\x57\x6F\x72\x6C\x64\x21')



try:
    with open('file.txt', 'r') as file:
        content = file.read()
        # Perform operations on the file content
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("Permission denied to open the file.")
except IOError:
    print("An I/O error occurred while working with the file.")
except Exception as e:
    print("An unexpected error occurred:", str(e))

