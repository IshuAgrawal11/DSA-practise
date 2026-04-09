roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C": 100, "D": 500, "M": 1000}
string = input("Enter roman numbers letters: ")
new = string.upper()
# 1. Validator: Check if all characters are valid Roman numerals
is_valid = all(char in roman for char in new)

if not is_valid:
    print("Error: Input contains invalid Roman numeral characters!")
else:
    number = 0
    for i in range(len(new)):
        if i + 1 < len(new) and roman[new[i]] < roman[new[i + 1]]:
            number -= roman[new[i]]
        else:
            number += roman[new[i]]

    print(f"The integer value is: {number}")

# Integer to roman
def intToRoman(num: int) -> str:
    mapping = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]   
    roman_numeral = ""
    
    for value, symbol in mapping:
        while num >= value:
            roman_numeral += symbol  
            num -= value             
            
    return roman_numeral

number = int(input("Enter an integer: "))
print(f"Roman Numeral: {intToRoman(number)}")


