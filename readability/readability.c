#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *text = get_string("Text: ");
    int Letters = 0;
    int Sentences = 0;
    int Words = 1; // +1 for the final word
    int length = strlen(text);
    char aux;
    for (int i = 0; i < length; i++)
    {
        if (isalpha(text[i]))
        {
            Letters++;
        }
        else if ((text[i] == '?') || (text[i] == '.') || (text[i] == '!'))
        {
            Sentences++;
        }
        else if (text[i] == ' ')
        {
            Words++;
        }
    }
    float L = ((float) Letters / (float) Words) * 100;
    float S = ((float) Sentences / (float) Words) * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = (int) round(index);

    if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}
