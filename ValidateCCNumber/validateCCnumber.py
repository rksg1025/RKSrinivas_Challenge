import re # importing regular expression package

for _ in range(int(input())): # for loop initiated by taking total number of records
    card_num = input() # taking each record

    withoutHiphen = bool(re.match(r"^[456]\d{15}$", card_num)) # checking each record having 456 as the initial digits of the card number consisting only 16 digits with out hyphen
    
    withHiphen = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", card_num)) # checking each record having 456 as the initial digits of the card number consisting only 16 digits with hyphen separated after every 4 digits
    
    card_num = card_num.replace("-", "") # removing hyphen
    
    finalCheck = bool(re.match(r"(?!.*(\d)(-?\1){3})", card_num)) # checking the card having more than 3 consecutive numbers
    
    if (withoutHiphen or withHiphen) and finalCheck: #if else condition to check the valid or invalid card numbers
        print("Valid")
    else:
        print("Invalid")