import random  # imports from the random module which will generate random characters
import string  # imports the string module for characters


def generate_password(length, include_digits=True, include_punctuation=True):
    """
    This generates a random password of given length
    :param length: The length of the password to be generated
    :param include_digits: Boolean flag indicating whether to include digits or not
    :param include_punctuation: Boolean flag indicating whether to include punctuation or not
    :return: The generated password
    """

    letters = string.ascii_letters
    if include_digits:
        letters += string.digits
    if include_punctuation:
        letters += string.punctuation
    password = ''.join(random.choice(letters) for i in range(length))
    return password


if __name__ == '__main__':
    length = int(input("How many characters should the password have?: "))
    include_digits = input("Should the password contain digits? Yes(y) No(n): ").lower() == 'y'
    include_punctuation = input("Should the password contain punctuation marks? Yes(y) No(n): ").lower() == 'y'
    password = generate_password(length, include_digits, include_punctuation)
    print(f"Your generated password is: {password}")
