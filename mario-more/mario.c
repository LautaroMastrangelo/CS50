#include <cs50.h>
#include <stdio.h>

void printBlocks(int);
int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height > 8 || height < 1);
    for (int i = 1; i < height + 1; i++)
    {
        for (int j = height - i; j > 0; j--)
        {
            printf(" ");
        }
        printBlocks(i);
        printf("\n");
    }
}
// Prints "lenght" hastags two times with two gaps between and no gaps at the end
void printBlocks(int lenght)
{
    for (int j = 0; j < 2; j++)
    {
        for (int i = 0; i < lenght; i++)
        {
            printf("#");
        }
        if (j == 0)
        {
            printf("  ");
        }
    }
}
