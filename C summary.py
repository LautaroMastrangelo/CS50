<C Sintaxis>
-printf
# #include using <  > at the start of the program
# to print variables use print("text %type text %type",variable1,variable2)
    # each variable will take place of the current %type in the toString (in order)
    # "%" MUST be followed by the correct type of variable:
    # %c = char ; %s = string ; %i = integer ; %li = long integer ; %f float [ig] ; %p = mem adress
# jump line \n
# // coments

-simple structures and types
# if, for, while. same as Java
# char, string, bool, int, float, long(64b integer), double (64b float)
# char elements uses '', while string use ""
# const type (constants)
# do while (repeat until) //especially useful when asking for data
# (float) variable //to convert a variable from int to float
# && and
# || or


-complex structures
# typedef struct
{
    types assigned
} nameStructure; (literally registers)
# &(variable) used to know a variable memory adress
# * used declare pointers ; type *(name) -> declare a pointer
# to acess a adress you can use the variable (name), to access to te contet of taht adress you use *(name)
# char *(name) -> this is how to create a string in C
# you can add displaces by adding numbers to a pointer (ej: *(variable + 1))
# uint8_t -> declare a byte

-functions
# type name(void) = function
# void name(type) = procedure
# if u want to put the main code at the beginning, you have to type the name of the function/procedure and end it with ;
    # example: int function(void);
# main (int argc, argv[]):
    # argv takes the parameters that you implement when you call te program (in an array)
    # argc takes the lengh of the array of parameters (automatically)

-array searching an sorting
# lineal search
# binary search


<C Style>
# () for condition go with space [ej: if ()]
# () for voids/functions go without it [ej function()]
# {} with the format:
...
if whatever
{
    code..
}
...

<C console codes>
#ls list (shows a list in the terminal like the one in the left)
#mv move (moves the content from a file to another)
#cd change directory (moves into the directory using the console, for example: cd folderX/ (acces to folderX))
#cp copy directory
#mkdir make directory (create a new directory)
#rm remove (avoid)
#rmdir remove directory (avoid)
#valgrind ./program

<libraries>
# cs50.h ; stdio.h ; string.h ; ctype.h ; stdlib.h
    # string:  strlen(string) (returns a string length)
    # string:  strcmp(string1, string2) returns 0 if strings are equals
    # ctype:   toupper(char) (returns a letter in uppercase)
    # stdlib:  x = malloc(space need) (books (space) bytes of memory for x)
    # stdlib:  free(variable): frees memory booked by malloc
    # stdlib:  strcpy(string1, string2): string1 = string2
    # stdlib?  atoi(char) converts a char number into a integer;
<file managment>
# fopen -> FILE *file = fopen (name.x )
# fclose
# fprintf
# fscanf
# fread
# fwrite
# fseek
