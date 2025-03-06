from cs50 import get_int


def main():
    card = get_int("card number: ")
    if (cardValidation(card)):
        print(cardType(card))
    else:
        print("INVALID")


def cardValidation(cardNumber):
    numberToMultiply = cardNumber // 10
    numberToSum = cardNumber
    total = 0
    digit = 0
    while (numberToMultiply > 0):
        digit = (numberToMultiply % 10) * 2
        if digit > 9:
            digit = (digit % 10) + (digit // 10)
        total += digit
        numberToMultiply = numberToMultiply // 100
    while (numberToSum > 0):
        total += numberToSum % 10
        numberToSum = numberToSum // 100
    if (total % 10) == 0:
        return True
    else:
        return False


def cardType(cardNumber):
    length = len(str(cardNumber))
    FN = int(str(cardNumber)[0])
    FTN = int(str(cardNumber)[:2])
    """ i guessed that there would be a simple way to get the first and first 2 numbers
    from a int in python and i search it in the first google result (page >bobbyhadz)
    """
    if (length == 15 and (FTN == 34 or FTN == 37)):
        return "AMEX"
    elif (length == 16 and (FTN > 50 and FTN < 56)):
        return "MASTERCARD"
    elif ((length == 13 or length == 16) and (FN == 4)):
        return "VISA"
    else:
        return "INVALID"


main()
