def check_character(word, index):
    char = word[index]
    if char.isalpha() == True:
        return "letter"
    elif char.isdigit() == True:
        return "digit"
    elif char.isspace() == True:
        return "white space"
    else:
        return "unkown"
     
if __name__ == "__main__":
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))