import string
import random

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    print("Random alphanumeric String is:", result_str)

password_length=int(input('ENTER YOUR PASSWORD LENGTH\n'))

get_random_alphanumeric_string(password_length)


