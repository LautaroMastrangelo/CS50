--libraries--
import >name< #imports a whole library
from >library< import functionToImport1, functionToImport2 #importes a part ofr the library

import cs50 #the name.function is to especify from where you want to use that function
x = cs50.get_int("x: ") #like the this. from java


--Base functions--
x = int(input()) #converts the string from input (base type) to a int
x = int(x) #you can converts variables itself lol
s = s.lower() #converts a string into lower case
s = s.upper() #converts a string into upper case
s = input().lower/upper #when giving a value, convert it into lower/upper case

sorted(DicVariable) #sorts a dictionary alphabetically
sorted(DicVariable, key=Value.get) #sorts a dictionary by values (last to first)
sorted(DicVariable, key=Value.get, reversed=True) #sorts by values (first to last)
sum(listVariable) #sums all the content from a numbers' list
len(listVariable) #returns the length of a list

--base methods--
listVariable.append #adds a value to a list



-csv- #V = variable
Vreader = csv.DictReader(Vfile) #reads the header of the csv file
Vreader = csv.reader(Vfile) #reads the whole csv file

for name in reader.fieldnames #loop through the file names (you probably want to skip the first one)
if name == reader.fieldnames[0] #this way you can skip the first column

for row in reader #loops through the rows(FILAS) in the csv
row[X] #represents a row value, for example [pepe, 1, asd] row[0] = pepe, row[2] = asd


--sys--
sys. #to acces the functions from the whole library
argv #array of strings loaded in console
exit() #quits the program returning a (value)

--SQL--
#sqlite3 implemented

sqlite3 newFile.db #open/create a file
.mode chooseMode(exp csv) #choose what file you are gonna read
.import fileName.fileType tableName #create a new table
.quit #exit the sql mode
.schema db #shows the fields and type of the from the db

primary key #created in the sheed and assigned there
foreign key #created from another seed and only used in the current one
AND OR
-usage-

SELECT columX, coulmY FROM tableName; #prints the colums form the table. select * -> selects the whole table
SELECT columX FROM tableName LIMIT X; #prints only the first X fields
SELECT columX FROM tableName ORDER BY x ASC/DESC; #prints the colum ordered by x
SELECT count(colum/*) FROM tableName; #prints the total of fields (without the header)
SELECT DISTINCT colum FROM tableName; #prints the fields without repeating them
SELECT count(*) FROM tableName WHERE colum = 'c'; #prints the total of fields where the data is 'c'
SELECT fieldX,count(*) FROM tableName GROUP BY fieldX; #prints the fields + the total amount of data in them
INSERT INTO tableName (field1, field2) VALUES ('x', 'y') #inserts a new colum with the values x and y in the fields 1 and 2
DELETE FROM tableName WHERE condition(example fieldX IS NULL); #deletes from the table all elements without a fieldx value
UPDATE tableName SET columX/* = 'value' WHERE condition(example fieldX IS NULL) #updates a row value
SELECT columX FROM tableName WHERE name LIKE '%part_of_its_name%' #searchs for elements with the corresponding like string in themo
-combined data-
SELEC * FROM shows WHERE id IN #this will show data stored in shows, but filtered by ratings
-> (SELECT show_id FROM ratings WHERE rating >= 6.0);

SELECT * FROM shows JOIN ratings ON shows.id = ratings.shows_id WHERE rating >= x;
#combine both tables by one in common value

-index-
CREATE INDEX indexName ON tableName (column)


--using sql in python--
from cs50 import SQL
dbVariable = SQL("sqlite///:file.db")
rows = dbVariable.execute("SELECT * AS n FROM file.db WHERE field = ?", fieldSearch)
row = rows[0]
