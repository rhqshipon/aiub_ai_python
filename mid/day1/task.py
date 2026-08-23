import string

a = input("Enter an input: ")

if a.isalpha():
    if a.isupper():
        print(f"The input >>> {a} <<< is in uppercase.")
    else:
        print(f"The input >>> {a} <<< is in lowercase.")

elif a.isdigit():
    print(f"The input >>> {a} <<< is a digit.")

elif a in string.punctuation:
    print(f"The input >>> {a} <<< is a punctuation character.")

else:
    print("Please enter a valid input.")