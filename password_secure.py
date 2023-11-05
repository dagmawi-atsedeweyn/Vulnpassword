#The program is written in Python. Its purpose is to test password strength   
#And help people make a stronger password so that they won't be vulnerable to brute force attack. 
#This helps them secure their private data. 


#Import important library
import random 

# Module Citation 
# https://docs.python.org/3/library/random.html 

#Password list Citation 
#Password list is imported from "https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt" 

# procedure to create a new password
def create_pw(sentence):
    # Make sure the sentence has at least 4 words
    if len(sentence.split()) < 4:
        print("The sentence should be at least 4 words long.")
        return None

    # Convert the sentence into a password
    special_key = ['!', '@', '%', '^', '&', '*', '$']
    password = "".join(word[0] for word in sentence.lower().split()) + str(random.randint(100, 999)) + random.choice(special_key)
    print("Your new password is:", password)
    return password
#procedure to match user password to commonly used password
def check_pw(user_pw):
    #Read and open file name   
    with open('pw_list.txt') as f_obj: 
        pw_list = f_obj.read() 
    for line in pw_list:
        if user_pw in pw_list: 
            print("Your password is vulnerable to brute force attack!") 
            return True
        else:
            print("Your password is not vulnerable to brute force attack.") 
            return False

#Ask user permission  
User = input("Do you want to check if your password is vulnerable to brute force attack? Type Y to continue or any other key to exit: ") 

if User.lower() == "y": 
    user_pw = input("Enter your password: ")
else: 
    exit() 
#Checking password vulnerability using a list
def check(user_pw):
    if check_pw(user_pw):
        ask = input("Do you want to create a new one? Type Y to continue or any other key to exit: ") 
        while ask.lower() == "y":
            # Ask the user for a sentence
            sentence = input("Enter a sentence that is at least 4 words long: ")
            password = create_pw(sentence)
            if password is not None:
                break
            ask = input("Do you want to try again? Type Y to continue or any other key to exit: ")

#call  the function
check(user_pw)
