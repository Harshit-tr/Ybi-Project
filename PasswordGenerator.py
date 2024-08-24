import random  # Importing the random module to generate random selections
import string  # Importing the string module to use predefined sets of characters

# Function to generate a password
def generatepassword(length):
    # Define possible characters for the password:
    # - string.ascii_letters includes both uppercase and lowercase letters
    # - string.digits includes numeric characters (0-9)
    # - string.punctuation includes special characters like !, @, #, etc.
    charcters = string.ascii_letters + string.digits + string.punctuation
    
    # Create the password by randomly selecting characters for the given length
    password = ''.join(random.choice(charcters) for i in range(length))
    
    # Return the generated password
    return password

# Main function to interact with the user
def main():
    try:
        # Ask the user to input the desired length of the password
        length = int(input("Enter the valid length for password:"))
        
        # Check if the user entered a valid length (greater than 0)
        if length < 1:
            print("Password must be at least 1.")  # Display error if length is invalid

        else:
            # Generate the password by calling the generatepassword function
            generatedpassword = generatepassword(length)
            
            # Display the generated password to the user
            print(f"Your generated password is {generatedpassword}")
    
    # Handle the case where the user enters something that is not a valid integer
    except ValueError:
        print("Enter a valid number for password generating")

# This ensures that the main function is called when the script is run directly
if __name__ == "__main__":
    main()

        