filename = "my_document.txt"
print(f"Attempting to work with the file: '{filename}'\n")

try:
    # The 'try' block attempts to open the file in read mode ('r').
    # This is the standard way to check for a file and read it at the same time.
    # If the file doesn't exist, Python will immediately raise a 'FileNotFoundError'
    # and jump to the 'except' block.
    with open(filename, 'r') as file:
        print(f"Success: '{filename}' already exists.")
        print("Reading contents...")
        
        # Read all the content from the file into a variable.
        content = file.read()
        
        print("\n--- File Content ---")
        if content:
            # If the file has content, print it.
            print(content)
        else:
            # If the file is empty, say so.
            print("[The file is empty]")
        print("--------------------")

except FileNotFoundError:
    # This 'except' block only runs if the file was not found in the 'try' block.
    print(f"Notice: '{filename}' does not exist. Creating it now.")
    
    # Open the file in write mode ('w'). This action creates a new, empty file.
    with open(filename, 'w') as file:
        # Write some initial lines of text to the new file.
        file.write("This is the first line of the new file.\n")
        file.write("Hello from the file manager script!\n")
        
    print(f"Successfully created and wrote initial content to '{filename}'.")
    print("You can run this script again to see it read the file.")

print("\nScript finished.")