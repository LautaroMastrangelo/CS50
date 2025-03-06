import csv
import sys


def main():

    # TODO: Check for command-line usage

    if len(sys.argv) != 3:
        print("Correct use: python dna.py databases/X.csv sequences/X.txt")
        sys.exit(1)
    # TODO: Read database file into a variable
        # i rather use "with open" insted of a file open variable
    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as file:
        file_DNA = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    length = 0
    auxList = []
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        length = len(reader.fieldnames)
        for name in reader.fieldnames:
            if name != reader.fieldnames[0]:  # first column which has name on it
                auxList.append(longest_match(file_DNA, name))

    # TODO: Check database for matching profiles
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip the first row with names
        for row in reader:
            found = True
            for i in range(length - 1):
                if (int(row[i + 1]) != auxList[i]):
                    found = False
                    break
            if found:
                print(row[0])
                break
        else:
            print("No match")
            

"""
I search a lot of information to do this problem. most of it from youtube.
im new at python and not very good with file handling so i found it quite hard
"""


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
