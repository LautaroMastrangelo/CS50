#include <cs50.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

void cardType(long);
bool creditCardValid(long);
int main(void)
{
    long creditCard = get_long("Number: ");

    if (creditCardValid(creditCard))
    {
        cardType(creditCard);
    }
    else
    {
        printf("INVALID\n");
    }
}
// Return the length of a number
int Get_numberLength(long number)
{
    int length = 0;
    long aux = number;
    while (aux > 0)
    {
        length++;
        aux = aux / 10;
    }
    return length;
}
// Prints the type of credit card (visa,mc,avex)
void cardType(long creditCard)
{
    int length = Get_numberLength(creditCard);
    long FN = creditCard;  // stands for FirstNumbers
    long OFN = creditCard; // stands for Only First Number (visa)
    for (int i = length; i > 2; i--)
    {
        FN = FN / 10;
    }
    for (int i = length; i > 1; i--)
    {
        OFN = OFN / 10;
    }
    if ((FN == 34 || FN == 37) && (length == 15))
    {
        printf("AMEX\n");
    }
    else if ((FN == 51 || FN == 52 || FN == 54 || FN == 55) && (length == 16))
    {
        printf("MASTERCARD\n");
    }
    else if ((OFN == 4) & (length == 13 || length == 16))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

// Return if a creditCard fits in Luhn’s Algorithm
bool creditCardValid(long creditCard)
{
    long digitToMultiply = creditCard / 10;
    long digitToSum = creditCard;
    int digit;
    int aux;
    int total = 0;
    while (digitToMultiply > 0)
    {
        digit = digitToMultiply % 10;
        digitToMultiply = digitToMultiply / 100;
        digit = digit * 2;
        if (digit > 9)
        {
            total += digit % 10;
            digit = digit / 10;
        }
        total += digit;
    }
    while (digitToSum > 0)
    {
        digit = digitToSum % 10;
        digitToSum = digitToSum / 100;
        total += digit;
    }
    total = total % 10;
    if (total == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
