// Implements a dictionary's functionality
#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int pos = hash(word);
    for (node *ptr = table[pos]; ptr != NULL; ptr = ptr->next)
    {
        if (strcasecmp(word, ptr->word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    char string[LENGTH + 1];
    FILE *dicToLoad = fopen(dictionary, "r");
    if (dicToLoad == NULL)
    {
        return (false);
    }
    while (fscanf(dicToLoad, "%s", string) == 1)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(dicToLoad);
            return false;
        }
        unsigned int position = hash(string);
        strcpy(n->word, string);
        n->next = table[position];
        table[position] = n;
    }
    fclose(dicToLoad);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    int aux = 0;
    node *auxList;
    for (int i = 0; i < N - 1; i++)
    {
        auxList = table[i];
        while (auxList != NULL)
        {
            aux++;
            auxList = auxList->next;
        }
    }
    return aux;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N - 1; i++)
    {
        if (table[i] != NULL)
        {
            node *tmp = table[i];
            for (node *ptr = table[i]->next; ptr != NULL; ptr = ptr->next)
            {
                free(tmp);
                tmp = ptr;
            }
            free(tmp);
        }
    }
    return true;
}
