#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

const int blockSize = 512;
typedef uint8_t byte;

int main(int argc, char *argv[])
{
    // check that everything was right
    if (argc != 2)
    {
        printf("Usage: ./recover card.raw\n");
        return 1;
    }
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Unable to open the file.\n");
        return 2;
    }

    // start of the code
    FILE *currentImage;
    byte block[blockSize];
    int filesCounter = 0;
    bool firstOpened = false;
    while (fread(block, sizeof(byte), blockSize, card) == blockSize)
    {
        // honestly i didnt undestood what brayan meant with the & 0xF0 == 0xe0 so i did it the traditional way
        if ((block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff) && (block[3] >= 0xe0 && block[3] <= 0xef))
        {
            if (firstOpened == false)
            {
                firstOpened = true;
            }
            else
            {
                fclose(currentImage);
            }
            // create a new file. open and check it, then write the block on it
            char fileName[8];
            sprintf(fileName, "%03i.jpg", filesCounter);
            currentImage = fopen(fileName, "w"); // declared earlier to avoid error in line 42
            if (currentImage == NULL)
            {
                printf("couldn't create a new image file\n");
                return 3;
            }
            fwrite(block, sizeof(byte), blockSize, currentImage);
            filesCounter++;
        }
        else if (firstOpened == true)
        {
            fwrite(block, sizeof(byte), blockSize, currentImage);
        }
    }
    fclose(currentImage); // last opened file
    fclose(card);
    return 0;
}
