def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    symbols = "'!?@#$%^&*()/\_-+=}{[]"'"'
    is_true = 0
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for i in s:
                if i not in symbols:
                    is_true += 1
        if is_true != 0:
            return True








main()