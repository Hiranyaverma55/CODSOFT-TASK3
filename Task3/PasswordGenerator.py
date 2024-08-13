import random
import string

def passwordGenerator(length):
   
    characters = string.punctuation + string.ascii_letters + string.digits 
   
    password = "".join(random.choice(characters) for item in range(length))
    return password

def Password():
   
    length = int(input("Enter the desired length of the password.: "))
    
    password = passwordGenerator(length)
   
    print("Generated password:", password)

if __name__ == "__main__":
    Password()

