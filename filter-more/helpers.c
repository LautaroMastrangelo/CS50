#include "helpers.h"
#include <math.h>
#include <stdio.h>

int GmatrixValue(int Y, int X, int height, int width, RGBTRIPLE image[height][width], int Gmatrix[3][3], int color);
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int currentBlue;
    int currentGreen;
    int currentRed;
    int average;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            currentBlue = image[i][j].rgbtBlue;
            currentGreen = image[i][j].rgbtGreen;
            currentRed = image[i][j].rgbtRed;
            /* I need to use this function to round the numbers correclty otherwise
            the program doesn't fit with the checkout */
            average = (int) round((currentBlue + currentGreen + currentRed) / 3.0);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int middle = width / 2;
    RGBTRIPLE aux;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < middle; j++)
        {
            /* Since dividing an odd number/2 gives the floor of the divison
            The loop will end at the middle swapping if even and not swapping if odd */
            aux = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = aux;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    int totalBlue;
    int totalRed;
    int totalGreen;
    int slots;
    RGBTRIPLE auxImage[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            totalBlue = 0;
            totalRed = 0;
            totalGreen = 0;
            slots = 0;
            // check the 9 adjacent pixels of the current one
            for (int k = i - 1; k <= i + 1; k++)
            {
                for (int z = j - 1; z <= j + 1; z++)
                {
                    // This if checks if the value isn't out of the image range
                    if (k > -1 && k < height && z > -1 && z < width)
                    {

                        totalBlue += image[k][z].rgbtBlue;
                        totalGreen += image[k][z].rgbtGreen;
                        totalRed += image[k][z].rgbtRed;
                        slots++;
                    }
                }
            }
            auxImage[i][j].rgbtGreen = (int) round((float) totalGreen / slots);
            auxImage[i][j].rgbtRed = (int) round((float) totalRed / slots);
            auxImage[i][j].rgbtBlue = (int) round((float) totalBlue / slots);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = auxImage[i][j];
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE auxMatrix[height][width];
    int GxMatrix[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int GyMatrix[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};
    int currentGx = 0;
    int currentGy = 0;
    double rootValue;
    int finalValue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            for (int z = 1; z <= 3; z++)
            {
                currentGx = GmatrixValue(i, j, height, width, image, GxMatrix, z);
                currentGy = GmatrixValue(i, j, height, width, image, GyMatrix, z);
                rootValue = sqrt(currentGx + currentGy);
                finalValue = round(rootValue);
                if (finalValue > 255)
                {
                    finalValue = 255;
                }
                if (z == 1)
                {
                    auxMatrix[i][j].rgbtRed = finalValue;
                }
                else if (z == 2)
                {
                    auxMatrix[i][j].rgbtGreen = finalValue;
                }
                else
                {
                    auxMatrix[i][j].rgbtBlue = finalValue;
                }
            }
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = auxMatrix[i][j];
        }
    }
    return;
}

// Returns a pixel color's Gmatrix value (1 red 2 green 3 blue)
int GmatrixValue(int Y, int X, int height, int width, RGBTRIPLE image[height][width], int Gmatrix[3][3], int color)
{
    int totalRed = 0;
    int totalBlue = 0;
    int totalGreen = 0;
    int Ymatrix = 0;
    int Xmatrix;
    int aux = 0;
    if (color > 3 || color < 1)
    {
        // the main program could end here with an error but since it is a function i don't know how to do it
        printf("expected 1 2 or 3\n");
        return 0;
    }
    for (int i = Y - 1; i < Y + 2; i++)
    {
        Xmatrix = 0;
        for (int j = X - 1; j < X + 2; j++)
        {
            /* Here i check to only consider values in range if not
            i wont add it (which is the same that add it multiplied by 0)*/
            if (i > -1 && i < height && j > -1 && j < width)
            {
                /* I don't think this is the best way to solve this program since its taking me long
                to make it, but i think its kinda reusable */
                if (color == 1)
                {
                    aux += image[i][j].rgbtRed * Gmatrix[Ymatrix][Xmatrix];
                }
                else if (color == 2)
                {
                    aux += image[i][j].rgbtGreen * Gmatrix[Ymatrix][Xmatrix];
                }
                else
                {
                    aux += image[i][j].rgbtBlue * Gmatrix[Ymatrix][Xmatrix];
                }
            }
            Xmatrix++;
        }
        Ymatrix++;
    }
    return (aux * aux);
}
