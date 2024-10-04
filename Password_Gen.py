#-----------------------------------------------------------------------------------------------#
#--------------------------------- PASSWORD GENERATOR ------------------------------------------#

import secrets
import string

class RandomPassword:
    
    
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    digits = string.digits
    special_char = string.punctuation
    
    all_char = upper_case + lower_case + digits + special_char

    @staticmethod
    def generate_random_password(len):
        len=int(input("\nEnter Lenght of the Password : "))
        password = [
            secrets.choice(RandomPassword.upper_case),
            secrets.choice(RandomPassword.lower_case),
            secrets.choice(RandomPassword.digits),
            secrets.choice(RandomPassword.special_char)
        ]
        
        for i in range(len-4):
            password.append(secrets.choice(RandomPassword.all_char))
        
        
        secrets.SystemRandom().shuffle(password)
        return ''.join(password)


if __name__ == "__main__":
    random_password = RandomPassword.generate_random_password(len)
    print("Random Password gGenerated is:", random_password,"\n")
