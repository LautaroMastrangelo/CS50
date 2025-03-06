#include <cs50.h>
#include <stdio.h>

int startingSize();
int finalSize();
int totalYears(int, int);
int main(void)
{
    // TODO: Prompt for start size
    int starting_size = startingSize();
    // TODO: Prompt for end size
    int final_size = finalSize(starting_size);
    // TODO: Calculate number of years until we reach threshold
    int years = totalYears(starting_size, final_size);
    // TODO: Print number of years
    printf("Years: %i\n", years);
}

// Ask for a number greater than 8
int startingSize()
{
    int starting_size;
    do
    {
        starting_size = get_int("please enter the starting size of the population (must be greater than 8): ");
    }
    while (starting_size < 9);
    return starting_size;
}

// Ask for a number greater than starting_size
int finalSize(int starting_size)
{
    int final_size;
    do
    {
        final_size = get_int("please enter the final size of the population (must be greater than %i): ", starting_size);
    }
    while (final_size < starting_size);
    return final_size;
}

// Return how many years it took the population to grow
int totalYears(int starting_size, int final_size)
{
    int years = 0;
    int current_size = starting_size;
    while (current_size < final_size)
    {
        current_size = current_size + (current_size / 3) - (current_size / 4);
        years++;
    }
    return years;
}
